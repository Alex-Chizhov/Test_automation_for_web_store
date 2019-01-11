from selenium.webdriver.support.ui import Select
import mysql.connector
import re


class AdminPanelHelper:

    def __init__(self, application):
        self.app = application


    def get_count_admin_menu(self):
        wd = self.app.wd
        wd.get('http://localhost/litecart/admin/')
        menu_items = wd.find_elements_by_xpath("//span[@class='name']")
        return len(menu_items)

    def add_new_product(self, product):
        wd = self.app.wd

        wd.find_element_by_xpath("//span[text()='Catalog']").click()
        wd.find_element_by_xpath("(//a[@class='btn btn-default'])[2]").click()
        wd.find_element_by_xpath("//input[@name='name[en]']").send_keys(product.name)
        wd.find_element_by_xpath("//label[@class='btn btn-default']").click()
        wd.find_element_by_xpath("//input[@value='1-3']").click()
        wd.find_element_by_xpath("//input[@name='date_valid_from']").send_keys(product.date_from)
        wd.find_element_by_xpath("//input[@name='date_valid_to']").send_keys(product.date_to)
        select = Select(wd.find_element_by_xpath("//select[@name='manufacturer_id']"))
        select.select_by_value("1")

        wd.find_element_by_xpath("//a[contains(text(),'Information')]").click()
        wd.find_element_by_xpath("//input[@name='short_description[en]']").send_keys(product.short_description)
        wd.find_element_by_xpath("//textarea[@name='description[en]']").send_keys(product.description)

        wd.find_element_by_xpath("//a[contains(text(),'Prices')]").click()
        wd.find_element_by_xpath("//input[@name='purchase_price']").send_keys(product.purchase_price)
        select = Select(wd.find_element_by_xpath("//select[@name='purchase_price_currency_code']"))
        select.select_by_value("USD")

        wd.find_element_by_xpath("//button[@value='Save']").click()

    def modify_last_product_name(self, product):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Catalog']").click()
        pencils = wd.find_elements_by_xpath("//i[@class='fa fa-pencil']")
        pencils[-1].click()
        name = wd.find_element_by_xpath("//input[@name='name[en]']")
        name.clear()
        name.send_keys(product.name)
        wd.find_element_by_xpath("//button[@value='Save']").click()

    def get_element_with_product_name_from_catalog_table(self, product_name):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Catalog']").click()
        return wd.find_element_by_xpath(f"//*[.='{product_name}']").text

    def remove_last_product(self):
        wd = self.app.wd

        wd.find_element_by_xpath("//span[text()='Catalog']").click()
        checkboxes = wd.find_elements_by_xpath("//tbody//input")
        checkboxes[-1].click()
        wd.find_element_by_xpath("//button[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()

    def get_product_count_from_catalog(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[text()='Catalog']").click()
        count = wd.find_element_by_xpath("//td[@colspan='5']")
        count = count.text
        number = re.search(r'Products: (.)', count)
        return int(number.group(1))

    def get_product_count_from_db(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="litecart"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id FROM lc_products")
        myresult = mycursor.fetchall()

        return len(myresult)
