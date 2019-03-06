from Parameter_Object.product import Product
import allure


@allure.feature('Remove last product from admin panel')
@allure.severity('Major')
def test_remove_last_product(appf_admin, db):
    with allure.step('Get product count from db'):
        count = db.get_product_count()
    if count == 0:
        with allure.step('There are no products in the catalog, and we add new one'):
            appf_admin.admin_panel.add_new_product(Product(
                name='test_name',
                date_from='01.01.2018',
                date_to='01.01.2020',
                short_description='short_description',
                description='description',
                USD=100
            ))
        count += 1
    with allure.step('Remove last product'):
        appf_admin.admin_panel.remove_last_product()
    with allure.step('Get product count from db again'):
        count_after = db.get_product_count()
    with allure.step('Comparison the length of the old products list and new one. Old list is less by one product'):
        assert count -1 == count_after