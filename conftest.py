from App.app import Application
from App.db import DbFixture
import pytest
import json
import os
import importlib
import jsonpickle

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--config', action='store', default='config.json')

conf_data = None

def load_config(file):
    global conf_data
    conf_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    if conf_data == None:
        with open(conf_file) as f:
            conf_data = json.load(f)
    return conf_data

@pytest.fixture(scope='session')
def appf_admin(request):
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--config'))['web']
    fixture = Application(browser)
    fixture.session.login_to_admin_panel(username=web_config["admin_name"], password=web_config["admin_password"])
    yield fixture
    fixture.session.logout_from_admin_panel()
    fixture.destroy()

@pytest.fixture(scope='session')
def appf_new_customer(request):
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--config'))['web']
    fixture = Application(browser)
    yield fixture
    fixture.destroy()

@pytest.fixture(scope='session')
def appf_customer(request):
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--config'))['web']
    fixture = Application(browser)
    fixture.session.user_login(email=web_config["user_email"], password=web_config["user_password"])
    yield fixture
    fixture.session.user_logout()
    fixture.destroy()

@pytest.fixture(scope='session')
def db(request):
    db_config = load_config(request.config.getoption('--config'))['db']
    dbfixture = DbFixture(
        host=db_config["host"],
        database=db_config["database"],
        user=db_config["user"],
        passwd=db_config['passwd']
    )
    yield dbfixture
    dbfixture.destroy()

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