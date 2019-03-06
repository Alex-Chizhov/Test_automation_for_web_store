import allure
from allure_commons.types import AttachmentType


@allure.feature('User login')
@allure.story('User login to website')
@allure.severity('blocker')
def test_user_login(appf_customer):
    username = appf_customer.user_account.get_username_from_hp()
    with allure.step('Make a screenshot'):
        allure.attach(appf_customer.wd.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    assert username == 'Nick'
