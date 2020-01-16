from behave import *
from src.objects.page import StaticLoggedOutHomePage
from src.objects.page import LoginPage
from src.data import Account


class LoginSteps:

    # Page Objects
    static_logged_out_homepage = StaticLoggedOutHomePage.StaticLoggedOutHomePage()
    login_page = LoginPage.LoginPage()

    @given('I am logged in on main page')
    def i_am_logged_in_on_main_page(self):
        self.static_logged_out_homepage.click_log_in()
        self.login_page.fill_username(Account.mail)
        self.login_page.fill_password(Account.password)


