import allure


@allure.feature('Filtering products by price')
@allure.severity('critical')
def test_filtering_products_by_price(appf_customer):
    list_products_prices = appf_customer.shop.get_filtering_products_by_price()
    assert list_products_prices == sorted(list_products_prices)
