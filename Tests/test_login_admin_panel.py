def test_login_to_admin_panel(appf_admin):
    assert appf_admin.admin_panel.get_count_admin_menu() == 17
