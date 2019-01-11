from Parameter_Object.product import Product

def test_remove_last_product(appf):
    appf.admin_panel.modify_last_product_name(
        Product(
            name='new_test_name'
    ))
    name = appf.admin_panel.get_element_with_product_name_from_catalog_table('new_test_name')
    assert name == 'new_test_name'