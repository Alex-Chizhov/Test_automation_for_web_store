from App.app import Application
import pytest
import json
import os
import importlib
import jsonpickle

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

def pytest_generate_tests(metafunc):
    # parameters from test_function, first is fixture and other parameters
    for fixture in metafunc.fixturenames:
        if fixture == 'test_data_create_account':
            testdata = load_from_module(fixture[10:])
            metafunc.parametrize(fixture, testdata, ids=[repr(i) for i in testdata])
        if fixture == 'json_users':
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[repr(i) for i in testdata])

def load_from_module(module):
    return importlib.import_module(f"Tests_data.{module}").testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"Tests_data\\{file}.json")) as f:
        return jsonpickle.decode(f.read())