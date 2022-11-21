import os.path
from os import system, listdir, curdir, PathLike, mkdir, chdir
from configparser import ConfigParser
from sys import exit


class GitAuto:
    
    CONFIG = ConfigParser()
    CFG_FILE = ".AUTOGitHub"

    def __init__(self):
        self.workspace = ""
        self.project = ""
        self.repo_url = ""

    def set_workspace(self, path: str | bytes | PathLike[str] | PathLike[bytes]):
        if os.path.isdir(path):
            self.workspace = path
            return self.workspace
        else:
            raise IOError(f"Found something wrong with the given path '{path}'.")

    def set_project(self, title: str, visibility: bool) -> bool:
        dirs = listdir(self.workspace)
        if title not in dirs:
            self.project = title
            return True
        else:
            return False

    def set_repo_url(self, github_url):
        self

    def initialize(self):
        # mkdir(f"{self.workspace}/{self.project}")
        system(f"git clone {self.repo_url}")
        chdir(f"{self.workspace}/{self.project}")
        with open(self.CFG_FILE, "w") as _:
            pass
        self.CONFIG.read(self.CFG_FILE)
        self.CONFIG.add_section("PROJECT")
        self.update_cfg("title", self.project)
        self.update_cfg("github", self.repo_url)
        self.write_cfg()
        self.__hide_config(True)
        self.exclude_cfg()

    def __hide_config(self, hide: bool):
        # hides the config file; would be written in .gitignore
        system("attrib {v}H{v}S{v}R {file}".format(v="+" if hide else "-", file=self.CFG_FILE))

    def update_cfg(self, key: str, value: str):
        self.CONFIG.set("PROJECT", key, value)

    def write_cfg(self):
        with open(self.CFG_FILE, "w") as cfg:
            self.CONFIG.write(cfg)

    def exclude_cfg(self):
        content = ""
        with open(".gitignore", "r") as file:
            content = file.read()
        content += f"\n#Invoked by AUTOGitHub\n{self.CFG_FILE}"
        with open(".gitignore", "w") as file:
            file.write(content)

    @staticmethod
    def update_repo(github_link: str):
        pass
