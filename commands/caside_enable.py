import sublime
import sublime_plugin

class CAsideEnableCommand(sublime_plugin.WindowCommand):
    def run(self, enable=True):
        from CAside.utils.caside_utils import setSettings, showStatus
        setSettings("enable", enable)
        if enable:
        	showStatus("CAside has been enabled")
        else:
        	showStatus("CAside has been disabled")
