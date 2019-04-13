from selenium.webdriver.support.ui import Select
class UserAccount:

    def __init__(self, application):
        self.app = application

    def create_account(self, user):
        wd = self.app.wd
        wd.get(f"http://{self.app.domain}/create_account")
        tax_id = wd.find_element_by_xpath("//input[@name='tax_id']")
        tax_id.clear()
        tax_id.send_keys(user.tax_id)
        company = wd.find_element_by_xpath("//input[@name='company']")
        company.clear()
        company.send_keys(user.company)
        firstname = wd.find_element_by_xpath("//input[@name='firstname']")
        firstname.clear()
        firstname.send_keys(user.firstname)
        lastname = wd.find_element_by_xpath("//input[@name='lastname']")
        lastname.clear()
        lastname.send_keys(user.lastname)

        select = Select(wd.find_element_by_xpath("//select[@name='country_code']"))
        select.select_by_value("US")
        select = Select(wd.find_element_by_xpath("//select[@name='zone_code']"))
        select.select_by_value("CA")
        email = wd.find_element_by_xpath(
            "//div[@class='form-group col-md-6 required']//input[@name='email']")
        email.clear()
        email.send_keys(user.email)

        password1 = wd.find_element_by_xpath("//div[@class='form-group col-md-6 required']//input[@name='password']")
        password1.clear()
        password1.send_keys(user.password)
        password2 = wd.find_element_by_xpath("//input[@name='confirmed_password']")
        password2.clear()
        password2.send_keys(user.password)
        wd.find_element_by_xpath("//input[@name='city']").clear()
        wd.find_element_by_xpath("//input[@name='postcode']").clear()


        wd.find_element_by_xpath("//button[@value='Create Account']").click()


    def get_username_from_hp(self):
        wd = self.app.wd
        wd.get(f"http://{self.app.domain}")
        username = wd.find_element_by_xpath("//li[@class='account dropdown']//a[@class='dropdown-toggle']").text
        return username