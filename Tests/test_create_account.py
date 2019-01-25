#from Tests_data.create_account import testdata as user
import pytest


#@pytest.mark.parametrize('user', testdata, ids=[repr(i) for i in testdata])
def test_create_account(appf_new_customer, test_data_create_account):
    user = test_data_create_account
    appf_new_customer.user_account.create_account(user)
    username = appf_new_customer.user_account.get_username_from_hp()
    appf_new_customer.session.user_logout()
    assert username == user.firstname

def test_create_account(appf_new_customer, json_users):
    user = json_users
    appf_new_customer.user_account.create_account(user)
    username = appf_new_customer.user_account.get_username_from_hp()
    appf_new_customer.session.user_logout()
    assert username == user.firstname