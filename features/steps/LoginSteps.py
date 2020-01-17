from behave import *
from src.data import Account


@given('I am logged in on main page')
def i_am_logged_in_on_main_page(context):

    context.static_logged_out_homepage.navigate_to()
    context.static_logged_out_homepage.click_log_in()
    context.login_page.fill_username(Account.mail)
    context.login_page.fill_password(Account.password)
    context.login_page.click_log_in()


