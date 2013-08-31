import sublime
from CAside.commands import *
from CAside.utils import *

def plugin_loaded():
    readSettings("CAside.sublime-settings")


class EventListener(sublime_plugin.EventListener):
    def sync_view(self):
        sublime.active_window().run_command("c_aside_sync")

    def on_activated(self, view):
        self.sync_view()

    def on_load(self, view):
        sublime.set_timeout(self.sync_view, getSettings("load_delay"))

    def on_new(self, view):
        sublime.set_timeout(self.sync_view, getSettings("load_delay"))
