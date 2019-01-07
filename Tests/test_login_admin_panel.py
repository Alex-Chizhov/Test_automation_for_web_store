def test_login_to_admin_panel(appf):
    appf.session.login_to_admin_panel(username='admin', password='admin')
    assert appf.admin_panel.get_count_admin_menu() == 17
    appf.session.logout_from_admin_panel()