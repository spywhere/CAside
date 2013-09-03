import sublime
from CAside.commands import *
from CAside.utils import *

def plugin_loaded():
    readSettings("CAside.sublime-settings")


class EventListener(sublime_plugin.EventListener):
    vid = None;

    def sync_view(self):
        sublime.active_window().run_command("c_aside_sync", {"group": self.vid[0], "view": self.vid[1]})

    def on_activated(self, view):
        self.vid = sublime.active_window().get_view_index(view)
        self.sync_view()

    def on_load(self, view):
        self.vid = sublime.active_window().get_view_index(view)
        sublime.set_timeout(self.sync_view, getSettings("load_delay"))

    def on_new(self, view):
        self.vid = sublime.active_window().get_view_index(view)
        sublime.set_timeout(self.sync_view, getSettings("load_delay"))
