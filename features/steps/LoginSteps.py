from behave import *
from src.objects.page import StaticLoggedOutHomePage
from src.objects.page import LoginPage
from src.data import Account


# Page Objects
static_logged_out_homepage = StaticLoggedOutHomePage.StaticLoggedOutHomePage()
login_page = LoginPage.LoginPage()


@given('I am logged in on main page')
def i_am_logged_in_on_main_page(context):
    static_logged_out_homepage.navigate_to()
    static_logged_out_homepage.click_log_in()
    login_page.fill_username(Account.mail)
    login_page.fill_password(Account.password)
    login_page.click_log_in()


