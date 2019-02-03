from selenium.webdriver.support.ui import Select
from Parameter_Object.user import User
from Parameter_Object.product import Product
import re
import random


class AdminPanelHelper:

    def __init__(self, application):
        self.app = application


    def get_count_admin_menu(self):
        wd = self.app.wd
        wd.get('http://localhost/litecart/admin/')
        menu_items = wd.find_elements_by_xpath("//span[@class='name']")
        return len(menu_items)

    def go_to_catalog_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/admin/?app=catalog&doc=catalog"):
            wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")

    def go_to_customers_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/admin/?app=customers&doc=customers"):
            wd.get("http://localhost/litecart/admin/?app=customers&doc=customers")

    def add_new_product(self, product):
        wd = self.app.wd

        self.go_to_catalog_page()
        wd.find_element_by_xpath("(//a[@class='btn btn-default'])[2]").click()
        wd.find_element_by_xpath("//input[@name='name[en]']").send_keys(product.name)
        wd.find_element_by_xpath("//label[@class='btn btn-default']").click()
        wd.find_element_by_xpath("//input[@value='1-3']").click()
        select = Select(wd.find_element_by_xpath("//select[@name='manufacturer_id']"))
        select.select_by_value("1")

        wd.find_element_by_xpath("//a[contains(text(),'Information')]").click()
        wd.find_element_by_xpath("//input[@name='short_description[en]']").send_keys(product.short_description)
        wd.find_element_by_xpath("//textarea[@name='description[en]']").send_keys(product.description)

        wd.find_element_by_xpath("//a[contains(text(),'Prices')]").click()
        wd.find_element_by_xpath("//input[@name='prices[USD]']").send_keys(product.USD)
        select = Select(wd.find_element_by_xpath("//select[@name='purchase_price_currency_code']"))
        select.select_by_value("USD")

        wd.find_element_by_xpath("//button[@value='Save']").click()

    def modify_last_product_name(self, product):
        wd = self.app.wd
        self.go_to_catalog_page()
        pencils = wd.find_elements_by_xpath("//i[@class='fa fa-pencil']")
        pencils[-1].click()
        name = wd.find_element_by_xpath("//input[@name='name[en]']")
        name.clear()
        name.send_keys(product.name)
        wd.find_element_by_xpath("//button[@value='Save']").click()

    def get_element_with_product_name_from_catalog_table(self, product_name):
        wd = self.app.wd
        self.go_to_catalog_page()
        return wd.find_element_by_xpath(f"//*[.='{product_name}']").text

    def remove_last_product(self):
        wd = self.app.wd
        self.go_to_catalog_page()
        checkboxes = wd.find_elements_by_xpath("//tbody//input")
        checkboxes[-1].click()
        wd.find_element_by_xpath("//button[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        wd.refresh()

    def remove_random_product(self):
        wd = self.app.wd
        self.go_to_catalog_page()
        wd.refresh()
        checkboxes = wd.find_elements_by_xpath("//tbody//input")
        index = random.randint(1, len(checkboxes)-1)
        checkboxes[index].click()
        wd.find_element_by_xpath("//button[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        wd.refresh()

    def get_product_count_from_catalog(self):
        wd = self.app.wd
        self.go_to_catalog_page()
        wd.refresh()
        count = wd.find_element_by_xpath("//td[@colspan='5']")
        count = count.text
        number = re.search(r'Products: (.+)', count)
        return int(number.group(1))


    def get_list_customers(self):
        wd = self.app.wd
        self.go_to_customers_page()
        wd.refresh()
        customers_list = []
        while True:
            rows = wd.find_elements_by_xpath("//tbody//tr")
            count = 1
            for row in rows:
                email = wd.find_element_by_xpath(f"//tbody/tr[{count}]/td[4]").text
                name = wd.find_element_by_xpath(f"//tbody/tr[{count}]/td[5]").text
                splited_name = name.split(' ')
                firstname = splited_name[0]
                lastname = splited_name[1]
                company = wd.find_element_by_xpath(f"//tbody/tr[{count}]/td[6]").text
                count += 1
                customers_list.append(User(company=company, firstname=firstname, lastname=lastname, email=email))
            try:
                wd.find_element_by_xpath("//a[.='Next']").click()
                count = 1
            except:
                break
        return customers_list

    def get_product_list(self):
        wd = self.app.wd
        self.go_to_catalog_page()
        product_list = []
        count = 0
        while True:
            try:
                wd.find_elements_by_xpath("//i[@class='fa fa-pencil']")[count].click()
            except:
                break
            name = wd.find_element_by_xpath("//input[@name='name[en]']").get_attribute('value')
            wd.find_element_by_xpath("//a[contains(text(),'Information')]").click()
            short_description = wd.find_element_by_xpath("//input[@name='short_description[en]']").get_attribute('value')
            description = wd.find_element_by_xpath("//textarea[@name='description[en]']").get_attribute('value')
            wd.find_element_by_xpath("//a[contains(text(),'Prices')]").click()
            USD = wd.find_element_by_xpath("//input[@name='prices[USD]']").get_attribute('value')
            wd.find_element_by_xpath("//button[@value='Cancel']").click()

            product_list.append(Product(name=name,short_description=short_description,description=description, USD=USD))
            count += 1
        return product_list