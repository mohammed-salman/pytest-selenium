import pytest
from selenium import webdriver

from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):

    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.firefox
    if request.param == "remote":
        web_driver = web_driver.Remote(command_executor="http://192.168.1.39:4444")
    request.cls.driver = web_driver
    yield
    web_driver.close()
