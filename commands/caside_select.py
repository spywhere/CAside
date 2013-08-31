import sublime
import sublime_plugin

class CAsideSelectCommand(sublime_plugin.WindowCommand):
    def run(self):
        from CAside.utils.caside_utils import setSettings, showStatus
        idx = sublime.active_window().get_view_index(sublime.active_window().active_view())
        group = idx[0]
        if group < 0:
        	group = 0
        setSettings("target_group", group)
        showStatus("Group " + str(group) + " was selected.")
