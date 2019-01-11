from app.app import Application
import pytest


@pytest.fixture(scope='session')
def appf(request):
    fixture = Application()
    fixture.session.login_to_admin_panel(username='admin', password='admin')
    yield fixture
    fixture.session.logout_from_admin_panel()
    fixture.destroy()

'''
@pytest.fixture()
def appf(request):
    fixture = AppFixture()
    request.addfinalizer(fixture.destroy)
    return fixture
'''