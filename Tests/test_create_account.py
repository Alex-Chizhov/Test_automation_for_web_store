from Parameter_Object.user import User
import pytest


testdata = [
User(tax_id='123456', company='My company', firstname='John10',
     lastname='Jonas', email='john13@mail.com', password='password'),

User(tax_id='123456', company='My company', firstname='Tom9',
     lastname='Jonas', email='tom13@mail.com', password='password')
]

@pytest.mark.parametrize('user', testdata, ids=[repr(i) for i in testdata])
def test_create_account(appf_new_customer, user):
    appf_new_customer.user_account.create_account(user)
    username = appf_new_customer.user_account.get_username_from_hp()
    appf_new_customer.session.user_logout()
    assert username == user.firstname