def test_login_to_admin_panel(appf):
    assert appf.admin_panel.get_count_admin_menu() == 17
