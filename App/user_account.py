from selenium.webdriver.support.ui import Select
class UserAccount:

    def __init__(self, application):
        self.app = application

    def create_account(self, user):
        wd = self.app.wd
        wd.get(f"http://{self.app.domain}/litecart/create_account")
        wd.find_element_by_xpath("//input[@name='tax_id']").send_keys(user.tax_id)
        wd.find_element_by_xpath("//input[@name='company']").send_keys(user.company)
        wd.find_element_by_xpath("//input[@name='firstname']").send_keys(user.firstname)
        wd.find_element_by_xpath("//input[@name='lastname']").send_keys(user.lastname)
        select = Select(wd.find_element_by_xpath("//select[@name='country_code']"))
        select.select_by_value("US")
        select = Select(wd.find_element_by_xpath("//select[@name='zone_code']"))
        select.select_by_value("CA")
        wd.find_element_by_xpath\
            ("//div[@class='form-group col-md-6 required']//input[@name='email']").send_keys(user.email)
        wd.find_element_by_xpath\
            ("//div[@class='form-group col-md-6 required']//input[@name='password']").send_keys(user.password)
        wd.find_element_by_xpath("//input[@name='confirmed_password']").send_keys(user.password)
        wd.find_element_by_xpath("//button[@value='Create Account']").click()


    def get_username_from_hp(self):
        wd = self.app.wd
        wd.get(f"http://{self.app.domain}/litecart")
        username = wd.find_element_by_xpath("//li[@class='account dropdown']//a[@class='dropdown-toggle']").text
        return username