import pytest
from Tests_data.product import testdata
import allure
import re

@allure.severity('Blocker')
@allure.feature('Add new product')
@pytest.mark.parametrize('product', testdata, ids=[repr(i) for i in testdata])
def test_add_new_product(appf_admin, product):
    with allure.step(f"Add product {product} in admin panel"):
        appf_admin.admin_panel.add_new_product(product)
    with allure.step(f"Get count of products {product} from search in admin panel"):
        name = re.match(r'name=(\S+)', str(product))
        clean_name = name.group(1)
        appf_admin.admin_panel.find_product_in_catalog_by_name(clean_name)
        products = appf_admin.admin_panel.get_count_product_row_from_catalog()
    with allure.step(f"Checking that searching product {product} return minimum 1 row with result"):
        assert products > 0