from Parameter_Object.user import User
import allure

@allure.feature('Matches db and ui users')
@allure.severity('Critical')
def test_matches_db_and_ui_users(db, appf_admin):
    with allure.step('Get user list from db'):
        db_users_list = db.get_user_list()
    with allure.step('Get user list from admin panel'):
        users_list_admin_panel = appf_admin.admin_panel.get_list_customers()
    with allure.step('The list of users from the database and from the admin panel are equal'):
        assert sorted(db_users_list, key=User.sort_key_firstname) == sorted(users_list_admin_panel, key=User.sort_key_firstname)