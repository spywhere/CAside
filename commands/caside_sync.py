import sublime
import sublime_plugin
import re

class CAsideSyncCommand(sublime_plugin.WindowCommand):
    def run(self, group=-1, view=-1):
        from CAside.utils.caside_utils import showStatus, getSettings, fileExists, isCooldown, getFileName, getFileSplit, getFileJoin
        if getSettings("enable") and isCooldown():
            if group < 0 and view < 0:
                if getSettings("debug"):
                    print("View is not a working file")
                return
            elif group < 0 or view < 0:
                idx = sublime.active_window().get_view_index(sublime.active_window().active_view())
            else:
                idx = [group, view]
            if idx[0] == getSettings("target_group"):
                if getSettings("debug"):
                    print("Working on opened group")
                return
            if getSettings("debug"):
                    print("Current view is " + str(idx[0]) + ":" + str(idx[1]))
            if group < 0 or view < 0:
                source_view = sublime.active_window().active_view()
            else:
                source_view = sublime.active_window().views_in_group(idx[0])[idx[1]]
            if source_view is None:
                return
            if source_view.file_name() is None:
                if getSettings("debug"):
                    print("Source file is not on the disk")
                return
            if source_view.file_name() is None:
                return
            file_info = getFileSplit(source_view.file_name())
            extensions = getSettings("extensions")
            file_name = None

            for ext in extensions:
                source_regex = re.search(ext["source_pattern"], file_info[1], re.I | re.M)
                header_regex = re.search(ext["header_pattern"], file_info[1], re.I | re.M)
                if source_regex is not None:
                    file_name = getFileJoin(file_info[0], source_regex.group(0)+ext["header_suffix"])
                if header_regex is not None:
                    file_name =  getFileJoin(file_info[0], header_regex.group(0)+ext["source_suffix"])
                if file_name is not None and fileExists(file_name):
                    break

            if file_name is None or not fileExists(file_name):
                if getSettings("debug"):
                    if file_name is None:
                        print("Pattern not matched")
                    else:
                        print("\"" + file_name + "\" is not found")
                return
            if getSettings("debug"):
                    print("Target file is \"" + file_name + "\"")
            if getSettings("target_group") > sublime.active_window().num_groups() - 1 and not getSettings("force_load"):
                if getSettings("debug"):
                    print("Target group is not visible")
                return
            target_view = sublime.active_window().find_open_file(file_name)
            alreadyOpen = True
            if target_view is None:
                target_view = sublime.active_window().open_file(file_name)
                alreadyOpen = False
            if getSettings("sync_view_index"):
                view_index = sublime.active_window().get_view_index(source_view)[1]
                if view_index >= len(sublime.active_window().views_in_group(getSettings("target_group"))):
                    view_index = len(sublime.active_window().views_in_group(getSettings("target_group")))-1
            else:
                view_index = 0
            sublime.active_window().set_view_index(target_view, getSettings("target_group"), view_index)
            if alreadyOpen and getSettings("auto_focus"):
                sublime.active_window().focus_group(getSettings("target_group"))
                sublime.active_window().focus_view(target_view)
            sublime.active_window().focus_view(source_view)
            if not alreadyOpen:
                showStatus(getFileName(file_name) + " opened in Group: " + str(getSettings("target_group")))
