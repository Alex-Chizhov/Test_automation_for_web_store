from App.app import Application
import pytest
import json


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')

with open("../config.json") as f:
    conf_data = json.load(f)

@pytest.fixture(scope='session')
def appf_admin(request):
    browser = request.config.getoption('--browser')
    fixture = Application(browser)
    fixture.session.login_to_admin_panel(username=conf_data["admin_name"], password=conf_data["admin_password"])
    yield fixture
    fixture.session.logout_from_admin_panel()
    fixture.destroy()

@pytest.fixture(scope='session')
def appf_new_customer(request):
    browser = request.config.getoption('--browser')
    fixture = Application(browser)
    yield fixture
    fixture.destroy()

@pytest.fixture(scope='session')
def appf_customer(request):
    browser = request.config.getoption('--browser')
    fixture = Application(browser)
    fixture.session.user_login(email=conf_data["user_email"], password=conf_data["user_password"])
    yield fixture
    fixture.session.user_logout()
    fixture.destroy()

'''
@pytest.fixture()
def appf(request):
    fixture = AppFixture()
    request.addfinalizer(fixture.destroy)
    return fixture
'''