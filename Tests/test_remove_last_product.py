from Parameter_Object.product import Product

def test_remove_last_product(appf_admin, db):
    count = db.get_product_count()
    if count == 0:
        appf_admin.admin_panel.add_new_product(Product(
            name='test_name',
            date_from='01.01.2018',
            date_to='01.01.2020',
            short_description='short_description',
            description='description',
            USD=100
        ))
        count += 1
    appf_admin.admin_panel.remove_last_product()
    count_after = db.get_product_count()

    assert count -1 == count_after