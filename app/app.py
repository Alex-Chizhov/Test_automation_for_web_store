from selenium import webdriver
from app.session import SessionHelper
from app.admin_panel import AdminPanelHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.admin_panel = AdminPanelHelper(self)

    def destroy(self):
        wd = self.wd
        wd.quit()