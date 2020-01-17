from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths


class LoginObject(BaseObject.BaseObject):

    # Locators
    username_input = [By.XPATH,'//input[contains(@class,\'js-username-field\')]']
    password_input = [By.XPATH, '//input[contains(@class,\'js-password-field\')]']
    login_button = [By.CSS_SELECTOR, 'button[type=\'submit\'][class*=\'EdgeButton\']']

    username_input_alt = [By.CSS_SELECTOR, 'input[name=\'session[username_or_email]\'][type=\'text\']']
    password_input_alt = [By.CSS_SELECTOR, 'input[name=\'session[password]\'][type=\'password\']']
    login_button_alt = [By.CSS_SELECTOR, '//form[@action=\'/sessions\']/div/div[3]/div']

    # Url
    path = Paths.login_page

    def validate_page(self):
        """
        Validates current page
        :return: True if username input is displayed
        """
        self.soft_wait_until_visible(self.username_input)
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
        if self.is_visible(self.username_input_alt, timeout=1):
            self.wait_until_visible_and_send_keys(self.username_input_alt, username)
        else:
            self.wait_until_visible_and_send_keys(self.username_input, username)

    def fill_password(self, password):
        """
        Fills in password
        :param password:
        """
        log.write_line('Filling in password with ' + password)
        if self.is_visible(self.password_input_alt, timeout=1):
            self.wait_until_visible_and_send_keys(self.password_input_alt, password)
        else:
            self.wait_until_visible_and_send_keys(self.password_input, password)

    def click_log_in(self):
        """
        Clicks on log in button
        """
        log.write_line('Clicking on Log In button')
        if self.is_visible(self.login_button_alt, timeout=1):
            self.click(self.login_button_alt)
        else:
            self.click(self.login_button)
