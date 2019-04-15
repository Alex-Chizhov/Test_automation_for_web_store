import pytest
from Tests_data.product import testdata
from Parameter_Object.product import Product
import allure

@allure.severity('Blocker')
@allure.feature('Add new product')
def test_add_new_product(appf_admin, db, check_ui):
    with allure.step("Get list of products from DB"):
        products_before = db.get_product_list()
    with allure.step(f"Add product in admin panel"):
        appf_admin.admin_panel.add_new_product(
            Product(
                name = 'Product name',
                short_description = 'Short description',
                description = 'Description',
                USD = '78',
                )
            )
    with allure.step("Get list of products from DB again"):
        product_after = db.get_product_list()
    with allure.step("Comparison the length of the old products list and new one"):
        assert len(products_before) +1 == len(product_after)

    if check_ui:
        with allure.step("Comparison sorted lists of product-objects with fully info about products"):
            assert sorted(product_after, key=Product.sort_key_name) == \
                   sorted(appf_admin.admin_panel.get_product_list(), key=Product.sort_key_name)