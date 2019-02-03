import pytest
from Tests_data.product import testdata
from Parameter_Object.product import Product


@pytest.mark.parametrize('product', testdata, ids=[repr(i) for i in testdata])
def test_add_new_product(appf_admin, db, check_ui, product):
    products_before = db.get_product_list()
    appf_admin.admin_panel.add_new_product(product)
    product_after = db.get_product_list()

    assert len(products_before) +1 == len(product_after)
    if check_ui:
        assert sorted(product_after, key=Product.sort_key_name) == \
               sorted(appf_admin.admin_panel.get_product_list(), key=Product.sort_key_name)