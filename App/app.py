from selenium import webdriver
from App.session import SessionHelper
from App.admin_panel import AdminPanelHelper
from App.user_account import UserAccount
from App.shop import ShopHelper
import os

class Application:

    def __init__(self, browser):
        self.domain = 'localhost'
        if browser == 'chrome':
            self.options = webdriver.ChromeOptions()
            self.options.add_extension(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\Extensions\\ChroPath_0_3_4_0.crx"))
            self.options.add_argument("--disable-infobars")
            self.wd = webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\Drivers\\chromedriver.exe"), options=self.options)
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'Ie':
            self.wd = webdriver.Ie()
        elif browser == 'remote':
            # selenoid
            self.domain = "192.168.1.122"
            capabilities = {
                "browserName": "chrome",
                "version": "72.0",
                "enableVNC": True,
                "enableVideo": False
            }
            self.wd = webdriver.Remote(command_executor="http://192.168.1.124:4444/wd/hub",
                                       desired_capabilities=capabilities)
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.admin_panel = AdminPanelHelper(self)
        self.user_account = UserAccount(self)
        self.shop = ShopHelper(self)

    def destroy(self):
        wd = self.wd
        wd.quit()