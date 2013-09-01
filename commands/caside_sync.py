import sublime
import sublime_plugin
import re

class CAsideSyncCommand(sublime_plugin.WindowCommand):
    def run(self):
        from CAside.utils.caside_utils import showStatus, getSettings, fileExists, isCooldown, getFileName, getFileSplit, getFileJoin
        if getSettings("enable") and isCooldown():
            idx = sublime.active_window().get_view_index(sublime.active_window().active_view())
            if idx[0] == getSettings("target_group"):
                if getSettings("debug"):
                    print("Working on opened group")
                return
            source_view = sublime.active_window().active_view()
            if source_view is None:
                return
            if source_view.file_name() is None:
                if getSettings("debug"):
                    print("Source file is not on the disk")
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
            target_view = sublime.active_window().find_open_file(file_name)
            alreadyOpen = True
            if target_view is None:
                target_view = sublime.active_window().open_file(file_name)
                alreadyOpen = False
            if getSettings("sync_view_index"):
                view_index = sublime.active_window().get_view_index(source_view)[1]
            else:
                view_index = 0
            sublime.active_window().set_view_index(target_view, getSettings("target_group"), view_index)
            if alreadyOpen and getSettings("auto_focus"):
                sublime.active_window().focus_group(getSettings("target_group"))
                sublime.active_window().focus_view(target_view)
            sublime.active_window().focus_view(source_view)
            if not alreadyOpen:
                showStatus(getFileName(file_name) + " opened in Group: " + str(getSettings("target_group")))
