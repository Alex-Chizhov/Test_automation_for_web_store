from App.app import Application
import pytest


@pytest.fixture(scope='session')
def appf_admin():
    fixture = Application()
    fixture.session.login_to_admin_panel(username='admin', password='admin')
    yield fixture
    fixture.session.logout_from_admin_panel()
    fixture.destroy()

@pytest.fixture(scope='session')
def appf_new_customer():
    fixture = Application()
    yield fixture
    fixture.destroy()

@pytest.fixture(scope='session')
def appf_customer():
    fixture = Application()
    fixture.session.user_login(email='nick20@mail.com', password='password')
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