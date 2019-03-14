import allure


@allure.feature('Add products to cart')
@allure.severity('blocker')
def test_add_products_to_cart(appf_customer):
    with allure.step("Get amount of products in cart"):
        count_before = appf_customer.shop.get_quantity_in_cart()
    with allure.step("Add 5 products in cart"):
        appf_customer.shop.add_products_to_cart_from_home_page(5)
    with allure.step("Get amount of products in cart again"):
        count_after = appf_customer.shop.get_quantity_in_cart()
    with allure.step(f"Comparison of amount products in cart before: {count_before} + 5 = after: {count_after}"):
        assert count_after == count_before + 5
