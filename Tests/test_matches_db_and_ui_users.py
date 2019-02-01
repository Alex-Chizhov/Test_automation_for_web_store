from Parameter_Object.user import User


def test_matches_db_and_ui_users(db, appf_admin):
    db_users_list = db.get_user_list()
    users_list_admin_panel = appf_admin.admin_panel.get_list_customers()
    assert sorted(db_users_list, key=User.sort_key_firstname) == sorted(users_list_admin_panel, key=User.sort_key_firstname)