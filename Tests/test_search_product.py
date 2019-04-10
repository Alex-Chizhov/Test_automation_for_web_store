import allure


@allure.feature('Search product')
@allure.severity('critical')
def test_search_product(appf_customer):
    product_name = 'Blue duck'
    with allure.step('Search product'):
        appf_customer.shop.search_product(product_name)
    with allure.step('Check that the title of the product is equal to the search phrase'):
        assert appf_customer.shop.get_title_of_product_from_product_page().lower() == product_name.lower()