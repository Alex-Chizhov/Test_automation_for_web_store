from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time
import re


class ShopHelper:

    def __init__(self, application):
        self.app = application

    def go_to_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith(f"{self.app.domain}"):
            wd.get(f"http://{self.app.domain}")

    def go_to_checkout_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/checkout"):
            wd.get(f"http://{self.app.domain}/checkout")

    def search_product(self, product_name):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_xpath("//input[@type='search']").send_keys(product_name + Keys.ENTER)

    def get_quantity_in_cart(self):
        wd = self.app.wd
        time.sleep(2)
        self.go_to_home_page()
        quantity = wd.find_element_by_xpath("//div[@id='cart']//span[@class='quantity']").text
        return int(quantity)

    def add_product_to_cart(self, quantity):
        wd = self.app.wd
        quantity_before = self.get_quantity_in_cart()

        if quantity:
            wd.find_element_by_xpath("//input[@name='quantity']").send_keys(Keys.CONTROL + 'a' + Keys.NULL,
                                                                            int(quantity))
        wd.find_element_by_xpath("//button[@name='add_cart_product']").click()
        count_after = quantity_before + quantity

        wait = WebDriverWait(wd, 10)
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(count_after)))

    def remove_all_products_from_cart(self):
        wd = self.app.wd
        self.go_to_checkout_page()
        if len(wd.find_elements_by_xpath("//a[contains(text(),'Back')]")) != 0:
            return
        while True:
            buttons = wd.find_elements_by_xpath("//button[@name='remove_cart_item']")
            if buttons == []:
                break
            button = buttons[0]
            button.click()
            wait = WebDriverWait(wd, 10)
            wait.until(EC.staleness_of(button))

    def add_products_to_cart_from_home_page(self, amount=1):
        wd = self.app.wd
        self.go_to_home_page()
        wait = WebDriverWait(wd, 10)
        for i in range(amount):
            products = wd.find_elements_by_xpath("//div[@id='box-popular-products']//div[contains(@class,'col-xs-6')]")
            products[random.randint(0, len(products)-1)].click()
            popup_window = wd.find_element_by_xpath("//div[@class='featherlight-content']")
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='add_cart_product']")))
            wd.find_element_by_xpath("//button[@name='add_cart_product']").click()
            wd.find_element_by_xpath("//div[@aria-label='Close']").click()
            wait.until(EC.staleness_of(popup_window))
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"), str(amount)))

    def checkout(self, user):
        wd = self.app.wd
        self.go_to_checkout_page()
        if len(wd.find_elements_by_xpath("//a[contains(text(),'Back')]")) != 0:
            return
        input_fields = ["firstname", "lastname", "address1", "postcode", "email", "city", "phone"]
        for field in input_fields:
            input_field = wd.find_element_by_xpath(f"//input[@name='{field}']")
            if input_field.get_attribute('value') == '':
                input_field.send_keys(user.__dict__[f'{field}'])

        wd.find_element_by_xpath("//h2").click()
        wd.refresh()
        wd.find_element_by_xpath("//button[@name='confirm_order']").click()
        wait = WebDriverWait(wd, 10)
        wait.until(EC.url_contains('order_success'))

    def get_message_from_order_success_page(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//h1").text

    def increase_quantity_item_in_cart(self, amount):
        wd = self.app.wd
        self.go_to_checkout_page()
        wait = WebDriverWait(wd, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@name='confirm_order']")))
        quantity = wd.find_element_by_xpath("//tr//input")
        amount_before = quantity.get_attribute('value')
        amount_after = int(amount_before) + int(amount)
        quantity.clear()
        quantity.send_keys(amount_after)
        wd.find_element_by_xpath("//i[contains(@class, 'refresh')]").click()

    def get_quantity_item_in_cart(self):
        wd = self.app.wd
        self.go_to_checkout_page()
        quantity = wd.find_element_by_xpath("//tr//input").get_attribute('value')
        return int(quantity)

    def add_product_multiple_times_to_cart(self, times=2):
        wd = self.app.wd
        self.go_to_home_page()
        product = wd.find_element_by_xpath("//div[@class='image-wrapper']")
        product.click()
        popup_window = wd.find_element_by_xpath("//div[@class='featherlight-content']")
        wait = WebDriverWait(wd, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='add_cart_product']")))
        add_to_cart_button = wd.find_element_by_xpath("//button[@name='add_cart_product']")
        for i in range(times):
            add_to_cart_button.click()
            wait.until(EC.invisibility_of_element((By.XPATH, "//div[@id='animated-cart-item']")))
        wd.find_element_by_xpath("//div[@aria-label='Close']").click()
        wait.until(EC.staleness_of(popup_window))

    def get_sum_in_cart_from_header(self):
        wd = self.app.wd
        self.go_to_home_page()
        sum = wd.find_element_by_xpath("//div[@id='cart']//span[@class='formatted_value']").text
        clean_sum = re.sub('\D', '', sum)
        return int(clean_sum)

    def get_price_first_product_from_checkout_page(self):
        wd = self.app.wd
        self.go_to_checkout_page()
        price = wd.find_element_by_xpath("//td[3]").text
        clean_price = re.sub('\D', '', price)
        return int(clean_price)

    def get_sum_in_cart_from_checkout_page(self):
        wd = self.app.wd
        self.go_to_checkout_page()
        price = wd.find_element_by_xpath("//td[5]").text
        clean_price = re.sub('\D', '', price)
        return int(clean_price)

    def get_title_of_product_from_product_page(self):
        wd = self.app.wd
        title = wd.find_element_by_xpath("//h1[@class='title']").text
        return title

    def get_number_popular_product_on_home_page(self):
        wd = self.app.wd
        self.go_to_home_page()
        products = wd.find_elements_by_xpath("//div[@id='box-popular-products']//div[contains(@class, 'products')]/div")
        return len(products)

    def get_filtering_products_by_price(self):
        wd = self.app.wd
        wd.get(f"http://{self.app.domain}/acme-corp-m-1/")
        wd.find_element_by_xpath("//span[.='Price']").click()
        prices = []
        while True:
            list_prices_obj = wd.find_elements_by_xpath("//span[@class='price']")
            for i in list_prices_obj:
                prices.append(int(re.sub('\D', '', i.text)))
            try:
                wd.find_element_by_xpath("//a[.='Next']").click()
                wait = WebDriverWait(wd, 5)
                wait.until(EC.staleness_of(list_prices_obj[0]))
            except:
                break
        return prices

    def get_filtering_products_by_name(self):
        wd = self.app.wd
        wd.get(f"http://{self.app.domain}/acme-corp-m-1/")
        wd.find_element_by_xpath("//span[.='Name']").click()
        names = []
        while True:
            list_prices_obj = wd.find_elements_by_xpath("//div[@class='name']")
            for i in list_prices_obj:
                names.append(i.text)
            try:
                wd.find_element_by_xpath("//a[.='Next']").click()
                wait = WebDriverWait(wd, 5)
                wait.until(EC.staleness_of(list_prices_obj[0]))
            except:
                break
        return names