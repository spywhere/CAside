import sublime
import sublime_plugin

class CAsideSelectCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        from CAside.utils.caside_utils import setSettings, showStatus
        idx = sublime.active_window().get_view_index(sublime.active_window().active_view())
        setSettings("target_group", idx[0])
        setSettings("target_view", idx[1])
        showStatus("View " + str(idx[1]) + " in group " + str(idx[0]) + " was selected.")
