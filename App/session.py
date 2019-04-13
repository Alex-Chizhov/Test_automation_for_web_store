class SessionHelper:

    def __init__(self, application):
        self.app = application

    def login_to_admin_panel(self, password, username):
        wd = self.app.wd
        wd.get(f"http://{self.app.domain}/admin")
        wd.find_element_by_xpath("//input[@placeholder='Username']").send_keys(username)
        wd.find_element_by_xpath("//input[@placeholder='Password']").send_keys(password)
        wd.find_element_by_xpath("//button[@value='Login']").click()
        # to make sure we are logged in
        wd.find_element_by_xpath("//div[@id='platform']")

    def logout_from_admin_panel(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//i[@class='fa fa-sign-out fa-lg']").click()

    def user_login(self, email, password):
        wd = self.app.wd
        wd.get(f"http://{self.app.domain}")
        wd.find_element_by_xpath("//li[@class='account dropdown']//a[@class='dropdown-toggle']").click()
        wd.find_element_by_xpath("//input[@placeholder='Email Address']").send_keys(email)
        wd.find_element_by_xpath("//input[@placeholder='Password']").send_keys(password)
        wd.find_element_by_xpath("//button[@value='Sign In']").click()

    def user_logout(self):
        wd = self.app.wd
        wd.get(f"http://{self.app.domain}")
        wd.find_element_by_xpath("//li[@class='account dropdown']//a[@class='dropdown-toggle']").click()
        wd.find_element_by_xpath("//ul[@class='dropdown-menu']//li[3]").click()
