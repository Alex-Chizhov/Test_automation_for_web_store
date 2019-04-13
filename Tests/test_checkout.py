import allure


@allure.feature('Checkout')
@allure.severity('blocker')
def test_Checkout(appf_new_customer, json_users):
    user = json_users
    with allure.step('Add products to cart'):
        appf_new_customer.shop.add_products_to_cart_from_home_page()
    with allure.step('Checkout'):
        appf_new_customer.shop.checkout(user)
    with allure.step("Check that message contains string 'successfully completed!'"):
        assert appf_new_customer.shop.get_message_from_order_success_page().__contains__("successfully completed!")