import pytest
import allure


@allure.feature('Create account using generator test data with special fixture')
@allure.severity('Blocker')
def test_create_account(appf_new_customer, test_data_create_account):
    user = test_data_create_account
    with allure.step(f'Create account {user}'):
        appf_new_customer.user_account.create_account(user)
    with allure.step('Get username from home page'):
        username = appf_new_customer.user_account.get_username_from_hp()
    with allure.step('Logout'):
        appf_new_customer.session.user_logout()
    with allure.step('Check that the username from the test data is equal to the username from the home page'):
        assert username == user.firstname

@allure.feature('Create account using Json(file) test data with special fixture')
@allure.severity('Blocker')
def test_create_account_json(appf_new_customer, json_users):
    import Generator.user
    user = json_users
    with allure.step(f'Create account {user}'):
        appf_new_customer.user_account.create_account(user)
    with allure.step('Get username from home page'):
        username = appf_new_customer.user_account.get_username_from_hp()
    with allure.step('Logout'):
        appf_new_customer.session.user_logout()
    with allure.step('Check that the username from the test data is equal to the username from the home page'):
        assert username == user.firstname