from Parameter_Object.product import Product
import allure

@allure.feature('Modify last product from admin panel')
@allure.severity('Major')
def test_modify_product_name(appf_admin):
    with allure.step('Modify last product name in admin panel'):
        appf_admin.admin_panel.modify_last_product_name(Product(name='new_test_name'))
    with allure.step('Get element with product name from catalog'):
        name = appf_admin.admin_panel.get_element_with_product_name_from_catalog_table('new_test_name')
    with allure.step('Check that the name is correct'):
        assert name == 'new_test_name'
