import sublime
import sublime_plugin

class CAsideSyncCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        from CAside.utils.caside_utils import showStatus
        showStatus("Opened")
        # idx = sublime.active_window().get_view_index(sublime.active_window().active_view())
