# GitHub Automation
# TODO: OBJECTIVES
# 1. Check for git installation
# 2. Check for internet connection
# 3. Ask for workspace path for the first time setup
# -  Ask for GitHub userid and password (and passcode if required) for the first time setup
# --
# 4. Ask for project/repo name, may be as the first argument later
# 5. Ask for public (default) or private, may be as the second argument later
# 6. Initialize the local with Git
# 7. Creates the repository with the project name in the remote
# 8.
import os.path
from sys import argv

from required.github_automate import GitHubAuto
from required.git_automate import GitAuto
from configparser import ConfigParser
from os import getenv, mkdir, chdir
# from selenium import webdriver

# DATA_FOLDER = os.path.join(getenv("APPDATA"), "/AUTOGitHub")
DATA_FOLDER = getenv("APPDATA") + "/AUTOGitHub"
DATA_FILE = DATA_FOLDER + "/AUTOGitHub.data.ini"
DATA: ConfigParser | None = None

PROJECT_NAME: str = ""
PROJECT_VISIBILITY: bool = True
# BROWSER = webdriver.Edge()


def user_input():
    response = input("Directory path for the all projects: ").strip()
    if response:
        if os.path.exists(response):
            return response
        else:
            print(f"You entered a path '{response}' that doesn't exists. Try again.")
            user_input()
    else:
        print("You have to give a folder location for where all the project repositories"
              " are going to reside. Give a full qualified (absolute) path for the folder to proceed.")
        user_input()


def ask_user(message: str,
             mandatory: bool = False):
    response = input(message).strip()
    if mandatory:
        if response:
            return response
        else:
            ask_user(message, mandatory)
    else:
        return response


if __name__ == '__main__':
    print(DATA_FOLDER)
    print(DATA_FILE)

    if not os.path.exists(DATA_FOLDER):
        mkdir(DATA_FOLDER)
        with open(DATA_FILE, "w") as file:
            # file.write("[ROOT]")
            pass

    DATA = ConfigParser()
    DATA.read(DATA_FILE)

    if not DATA.has_option("ROOT", "workspace"):
        base_dir = user_input()
        DATA.add_section("ROOT")
        DATA.set("ROOT", "workspace", base_dir)
        with open(DATA_FILE, "w") as file:
            DATA.write(file)

    chdir(DATA.get("ROOT", "workspace"))

    try:
        PROJECT_NAME = argv[1]
    except IndexError:
        print("You must have to specify the name of the new project as the first argument."
              "\nTry Again.")
        # exit()

    try:
        if argv[2] in ["-p", "--p", "p", "-private", "--private", "private"]:
            PROJECT_VISIBILITY = False
    except IndexError:
        PROJECT_VISIBILITY = True

    github = GitHubAuto()
    github.open()
    github.new_repo()
    # OTP Verification
    ask_otp = int(ask_user("Enter the OTP sent to your registered mobile/email: ", mandatory=True))
    github.verify_otp(otp=ask_otp)

