from Parameter_Object.user import User


def test_create_account(appf_new_customer):
    appf_new_customer.user_account.create_account(User(
        tax_id='123456',
        company='My company',
        firstname='Nick',
        lastname='Jonas',
        email='nick20@mail.com',
        password='password'
    ))
    username = appf_new_customer.user_account.get_username_from_hp()
    assert username == 'Nick'