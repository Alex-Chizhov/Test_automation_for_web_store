from Parameter_Object.product import Product

def test_remove_last_product(appf):
    count = appf.admin_panel.get_product_count_from_catalog()
    if count == 0:
        appf.admin_panel.add_new_product(Product(
            name='test_name',
            date_from='01.01.2018',
            date_to='01.01.2020',
            short_description='short_description',
            description='description',
            purchase_price=100
        ))
        count += 1
    appf.admin_panel.remove_last_product()
    count_after = appf.admin_panel.get_product_count_from_catalog()

    assert count -1 == count_after