import allure


@allure.feature('Search product')
@allure.severity('critical')
def test_search_product(appf_customer):
    product_name = 'Blue duck'
    appf_customer.shop.search_product(product_name)
    assert appf_customer.shop.get_title_of_product_from_product_page().lower() == product_name.lower()