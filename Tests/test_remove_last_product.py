import time

def test_remove_last_product(appf):
    product_count_before = appf.admin_panel.get_product_count_from_db()
    appf.admin_panel.remove_last_product()
    time.sleep(1)
    product_count_after = appf.admin_panel.get_product_count_from_db()

    assert product_count_before  == product_count_after + 1