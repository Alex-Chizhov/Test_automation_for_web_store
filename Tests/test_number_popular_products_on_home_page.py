import allure


@allure.feature('Popular product on home page')
@allure.severity('critical')
def test_search_product(appf_customer):
    with allure.step('Get number of popular product on home page'):
        products = appf_customer.shop.get_number_popular_product_on_home_page()
    with allure.step('Check that the number of popular product = 10'):
        assert products == 10