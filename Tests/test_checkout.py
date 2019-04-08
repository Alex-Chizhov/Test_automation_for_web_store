from Parameter_Object.user import User
import allure


@allure.feature('Checkout')
@allure.severity('blocker')
def test_Checkout(appf_new_customer):
    with allure.step('Add products to cart'):
        appf_new_customer.shop.add_products_to_cart_from_home_page()
    with allure.step('Checkout'):
        appf_new_customer.shop.checkout(
            User(
                tax_id='123456',
                company='Apple',
                firstname='Bob',
                lastname='Jephson ',
                email='jephson@email.com',
                password='password',
                address1='1515 Main St, Billings, MT 59105,',
                city='Montana',
                phone='+1 406-896-9680',
                postcode='105043'
             ))