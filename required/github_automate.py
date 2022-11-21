from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class GitHubAuto:

    GH_LOGIN = "https://github.com/login"
    GH_ELEMENTS = {
        "new_button": "",
        "title_entry": "",
        "desc_entry": "",
        "readme": "",
        "gitignore": "",
        "license": "",
        "create": "",
        "copy": "",
    }

    def __init__(self, browser: WebDriver | None = None):
        # self.browser = browser
        self.browser: WebDriver | None = None
        self.__user = {
            "id": "passion-lab",
            "pw": "SS$GitHub@1319",
            "pc": ""
        }
        self.github = ""
        self.branch = ""

    def open(self):
        self.browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.browser.get(self.GH_LOGIN)

    def new_repo(self):
        self.browser.find_element(By.ID, "login_field").send_keys(self.__user["id"])
        self.browser.find_element(By.ID, "password").send_keys(self.__user["pw"])
        self.browser.find_element(By.NAME, "commit").click()

    def verify_otp(self, otp):
        self.browser.find_element(By.NAME, "otp").send_keys(otp)
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

