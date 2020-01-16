from behave import *
from src.objects.page import StaticLoggedOutHomePage
from src.objects.page import LoginPage
from src.helpers import DataParser

class LoginSteps:

    # Page Objects
    static_logged_out_homepage = StaticLoggedOutHomePage.StaticLoggedOutHomePage()
    login_page = LoginPage.LoginPage()

    # Data Objects
    account = DataParser.parse_data_object('Account')

    @given('I am logged in on main page')
    def step_impl(self):
        self.static_logged_out_homepage.click_log_in()
        self.login_page.fill_username(self.account['MisterTester']['mail'])
        self.login_page.fill_password(self.account['MisterTester']['password'])


