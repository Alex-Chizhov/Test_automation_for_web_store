from selenium import webdriver
from App.session import SessionHelper
from App.admin_panel import AdminPanelHelper
from App.user_account import UserAccount

class Application:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_extension('..\\Extensions\\ChroPath_0_3_4_0.crx')
        self.wd = webdriver.Chrome(options=self.options)
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.admin_panel = AdminPanelHelper(self)
        self.user_account = UserAccount(self)

    def destroy(self):
        wd = self.wd
        wd.quit()