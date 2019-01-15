from selenium import webdriver
from app.session import SessionHelper
from app.admin_panel import AdminPanelHelper
from app.user_account import UserAccount

class Application:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_extension('..\\extensions\\ChroPath_0_3_4_0.crx')
        self.wd = webdriver.Chrome(options=self.options)
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.admin_panel = AdminPanelHelper(self)
        self.user_account = UserAccount(self)

    def destroy(self):
        wd = self.wd
        wd.quit()