from Parameter_Object.user import User
import pytest
import random
import string

def random_string(maxlen):
    symbol = string.ascii_letters + string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(1,maxlen))])

def random_digits(maxlen):
    symbol = string.digits
    return ''.join([random.choice(symbol) for i in range(random.randrange(1,maxlen))])

testdata = [
User(tax_id=random_digits(6), company=random_string(10), firstname=random_string(10),
     lastname=random_string(6), email=random_string(10)+'@mail.com', password=random_string(8))
    for i in range(10)
]

@pytest.mark.parametrize('user', testdata, ids=[repr(i) for i in testdata])
def test_create_account(appf_new_customer, user):
    appf_new_customer.user_account.create_account(user)
    username = appf_new_customer.user_account.get_username_from_hp()
    appf_new_customer.session.user_logout()
    assert username == user.firstname