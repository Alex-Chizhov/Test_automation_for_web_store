def test_create_account(appf_customer):
    username = appf_customer.user_account.get_username_from_hp()
    assert username == 'Nick'
