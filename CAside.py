import sublime
from CAside.commands import *
from CAside.utils import *

def plugin_loaded():
    readSettings("CAside.sublime-settings")


class EventListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        view.run_command("c_aside_sync")
