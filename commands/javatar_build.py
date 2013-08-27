import sublime
import sublime_plugin
import re
from Javatar.utils import *


class JavatarBuildCommand(sublime_plugin.WindowCommand):
    build_list = [["Project", "Build all classes in project"], ["Package", "Build all classes in current package"], ["Current Class", "Build current class"], ["Test", "Test output view"]]

    def buildFile(self, file):
        if isJava(file):
            print(file)
            window = sublime.active_window()
            buildScript = getSettings("build_system")
            buildScript = re.sub("\\$file_path", getPath("parent", file), buildScript)
            buildScript = re.sub("\\$file_name", getPath("name", file), buildScript)
            buildScript = re.sub("\\$file", file, buildScript)
            buildScript = re.sub("\\$packages", sublime.packages_path(), buildScript)
            if window.project_file_name() is not None:
                buildScript = re.sub("\\$project_path", getPath("parent", window.project_file_name()), buildScript)
                buildScript = re.sub("\\$project_name", getPath("name", window.project_file_name()), buildScript)
                buildScript = re.sub("\\$project", window.project_file_name(), buildScript)
            sublime.active_window().run_command("exec", {getSettings("build_command"): buildScript})
        return isJava(file)

    def buildAll(self, dir):
        build = False
        for path, subdirs, files in os.walk(dir):
            for filename in files:
                if isJava(getPath("join", path, filename)):
                    build = True
                    self.buildFile(getPath("join", path, filename))
        return build

    def run(self, type=""):
        view = sublime.active_window().active_view()
        if type == "project":
            if isProject() or isFile():
                if not self.buildAll(getPackageRootDir()):
                    sublime.error_message("No class to build")
            else:
                sublime.error_message("Unknown package location")
        elif type == "package":
            if isProject() or isFile():
                if not self.buildAll(getPath("current_dir")):
                    sublime.error_message("No class to build")
            else:
                sublime.error_message("Unknown package location")
        elif type == "class":
            if isFile():
                if not self.buildFile(view.file_name()):
                    sublime.error_message("Current file is not Java")
            else:
                sublime.error_message("Unknown class location")
        elif type == "test":
            window = sublime.active_window()
            panel = window.create_output_panel("Javatar")
            window.run_command("show_panel", {"panel": "output.Javatar"})
            panel.run_command("insert_snippet", {"contents": "Hello, World?"})
            panel.set_read_only(True)
        else:
            view.window().show_quick_panel(self.build_list, self.build)

    def build(self, index=-1):
        if index == 0:
            self.run("project")
        elif index == 1:
            self.run("package")
        elif index == 2:
            self.run("class")
        elif index == 3:
            self.run("test")
