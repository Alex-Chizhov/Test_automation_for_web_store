import allure


@allure.feature('Login to admin panel')
@allure.severity('Blocker')
def test_login_to_admin_panel(appf_admin):
    with allure.step('Check that login to admin panel was successful'):
        assert appf_admin.admin_panel.get_count_admin_menu() == 17
