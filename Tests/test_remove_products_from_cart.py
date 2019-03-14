import allure


@allure.feature('Remove products from cart')
@allure.severity('blocker')
def test_remove_products_from_cart(appf_customer):
    with allure.step("Get amount of products in cart"):
        count_before = appf_customer.shop.get_quantity_in_cart()
    with allure.step("Remove all products from cart"):
        appf_customer.shop.remove_all_products_from_cart()
    with allure.step("Get amount of products in cart again"):
        count_after = appf_customer.shop.get_quantity_in_cart()
    with allure.step(f"Amount of products in cart before should be = 0. Before removing:{count_before} after:{count_after}"):
        assert count_after == 0
