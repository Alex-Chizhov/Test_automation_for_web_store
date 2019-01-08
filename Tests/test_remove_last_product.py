def test_remove_last_product(appf):
    product_count_before = appf.admin_panel.get_product_count_from_db()
    appf.session.login_to_admin_panel(username='admin', password='admin')
    appf.admin_panel.remove_last_product()
    appf.session.logout_from_admin_panel()
    product_count_after = appf.admin_panel.get_product_count_from_db()

    assert product_count_before  == product_count_after + 1