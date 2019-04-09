import allure


@allure.feature('Add the same product multiple times')
@allure.severity('critical')
def test_add_same_products_multiple_times_to_cart(appf_customer):
    quantity = 2
    appf_customer.shop.remove_all_products_from_cart()
    with allure.step("Add the same product 2 times"):
        appf_customer.shop.add_product_multiple_times_to_cart(quantity)
    with allure.step("Get amount of products in cart again, and price of product and it's sum"):
        amount_product_in_cart = appf_customer.shop.get_quantity_in_cart()
        price = appf_customer.shop.get_price_first_product_from_checkout_page()
        sum = appf_customer.shop.get_sum_in_cart_from_checkout_page()
    with allure.step(f"Amount of products in cart should be equal = {amount_product_in_cart}"):
        assert amount_product_in_cart == quantity
    with allure.step(f"The sum of {quantity} products = price of 1 product * {quantity}"):
        assert price * quantity == sum