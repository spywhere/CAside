import sublime


STATUS = "CAside"
SETTINGS = None
SETTINGSBASE = None


def readSettings(config):
    global SETTINGS, SETTINGSBASE
    SETTINGSBASE = config
    SETTINGS = sublime.load_settings(SETTINGSBASE)


def getSettings(key, val=None):
    global SETTINGS
    return SETTINGS.get(key, val)


def setSettings(key, value):
    global SETTINGS, SETTINGSBASE
    SETTINGS.set(key, value)
    sublime.save_settings(SETTINGSBASE)


def showStatus(text, delay=None):
    if delay is None:
        delay = getSettings("status_delay", 5000)
    view = sublime.active_window().active_view()
    view.set_status(STATUS, text)
    if delay >= 0:
        sublime.set_timeout(hideStatus, delay)


def hideStatus():
    view = sublime.active_window().active_view()
    view.erase_status(STATUS)