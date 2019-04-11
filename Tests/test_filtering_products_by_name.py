import allure


@allure.feature('Filtering products by name')
@allure.severity('critical')
def test_filtering_products_by_name(appf_customer):
    list_products_names = appf_customer.shop.get_filtering_products_by_price()
    assert list_products_names == sorted(list_products_names)