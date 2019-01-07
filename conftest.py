from app.app import Application
import pytest


@pytest.fixture()
def appf(request):
    fixture = Application()
    yield fixture
    fixture.destroy()

'''
@pytest.fixture()
def appf(request):
    fixture = AppFixture()
    request.addfinalizer(fixture.destroy)
    return fixture
'''