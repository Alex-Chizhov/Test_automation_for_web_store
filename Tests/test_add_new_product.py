from Parameter_Object.product import Product


def test_add_new_product(appf_admin, db):
    product_count_before = db.get_product_count_from_db()
    appf_admin.admin_panel.add_new_product(Product(
        name='test_name',
        date_from='01.01.2018',
        date_to='01.01.2020',
        short_description='short_description',
        description='description',
        purchase_price=100
    ))
    product_count_after = db.get_product_count_from_db()

    assert product_count_before + 1 == product_count_after