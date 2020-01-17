from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths

class LoginObject(BaseObject.BaseObject):

    # Locators
    username_input = [By.XPATH,'//input[contains(@class,\'js-username-field\')]']
    password_input = [By.XPATH, '//input[contains(@class,\'js-password-field\')]']
    login_button = [By.CSS_SELECTOR, 'button[type=\'submit\'][class*=\'EdgeButton\']']

    # Url
    path = Paths.login_page

    def validate_page(self):
        """
        Validates current page
        :return: True if username input is displayed
        """
        return self.is_visible(self.username_input)

    def navigate_to(self):
        """
        Navigates to current page
        """
        self.navigate_to_by_url(self.url+self.path)

    def fill_username(self, username):
        """
        Fills in username
        :param username:
        """
        log.write_line('Filling in username with ' + username)
        self.wait_until_visible_and_send_keys(self.username_input, username)

    def fill_password(self, password):
        """
        Fills in password
        :param password:
        """
        log.write_line('Filling in password with ' + password)
        self.wait_until_visible_and_send_keys(self.password_input, password)

    def click_log_in(self):
        """
        Clicks on log in button
        """
        log.write_line('Clicking on Log In button')
        self.find_element(self.login_button).click()
