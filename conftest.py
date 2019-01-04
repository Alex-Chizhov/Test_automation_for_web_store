from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def wd():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()