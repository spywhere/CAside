import sublime
from CAside.utils import *
from CAside.commands import *


def plugin_loaded():
    config = sublime.load_settings("CAside.sublime-settings")
    readSettings(config)
    hideStatus()


class EventListener(sublime_plugin.EventListener):
    def on_new(self, view):
        hideStatus()

    def on_activated(self, view):
        hideStatus()

    def on_load(self, view):
        hideStatus()

    def on_post_save(self, view):
        hideStatus()

    def on_clone(self, view):
        hideStatus()
