from Config.config import TestData
from Pages.Basepage import BasePage
from Pages.LoginPage import LoginPage
from Test.test_base import Basetest


class TestLogin(Basetest):
    def test_signup_link(self):
        self.loginPage = LoginPage(self.driver)
        flage = self.loginPage.is_signup_link_exist()
        assert flage
        # self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    def test_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.TITLE)
        assert title == TestData.TITLE

    def test_login_page(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
