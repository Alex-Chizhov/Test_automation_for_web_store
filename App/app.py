from selenium import webdriver
from App.session import SessionHelper
from App.admin_panel import AdminPanelHelper
from App.user_account import UserAccount
from App.shop import ShopHelper
import os

class Application:

    def __init__(self, browser):
        if browser == 'chrome':
            self.options = webdriver.ChromeOptions()
            self.options.add_extension(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\Extensions\\ChroPath_0_3_4_0.crx"))
            self.options.add_argument("--disable-infobars")
            self.wd = webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\Drivers\\chromedriver.exe"), options=self.options)
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'Ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.wd.implicitly_wait(4)
        self.session = SessionHelper(self)
        self.admin_panel = AdminPanelHelper(self)
        self.user_account = UserAccount(self)
        self.shop = ShopHelper(self)

    def destroy(self):
        wd = self.wd
        wd.quit()