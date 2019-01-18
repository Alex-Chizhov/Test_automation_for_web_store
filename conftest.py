from App.app import Application
import pytest
import json
import os


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--config', action='store', default='config.json')

conf_data = None

@pytest.fixture(scope='session')
def appf_admin(request):
    global conf_data
    browser = request.config.getoption('--browser')
    conf_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--config'))
    if conf_data == None:
        with open(conf_file) as f:
            conf_data = json.load(f)
    fixture = Application(browser)
    fixture.session.login_to_admin_panel(username=conf_data["admin_name"], password=conf_data["admin_password"])
    yield fixture
    fixture.session.logout_from_admin_panel()
    fixture.destroy()

@pytest.fixture(scope='session')
def appf_new_customer(request):
    global conf_data
    browser = request.config.getoption('--browser')
    conf_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--config'))
    if conf_data == None:
        with open(conf_file) as f:
            conf_data = json.load(f)
    fixture = Application(browser)
    yield fixture
    fixture.destroy()

@pytest.fixture(scope='session')
def appf_customer(request):
    global conf_data
    browser = request.config.getoption('--browser')
    conf_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--config'))
    if conf_data == None:
        with open(conf_file) as f:
            conf_data = json.load(f)
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