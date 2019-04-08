import allure


@allure.feature('Increase quantity item in cart')
@allure.severity('Critical')
def test_increase_quantity_item_in_cart(appf_new_customer):
    with allure.step('Add product to cart'):
        with allure.step('Addition product to cart. Increase quantity of that product in cart'):
            appf_new_customer.shop.add_products_to_cart_from_home_page(1)
            appf_new_customer.shop.increase_quantity_item_in_cart(2)
        with allure.step("Check that quantity are changed"):
            assert appf_new_customer.shop.get_quantity_item_in_cart() == 3