from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths


class StaticLoggedOutHomeObject(BaseObject.BaseObject):

    # Locators
    login_button = [By.CSS_SELECTOR, 'a[class*=\'StaticLoggedOutHomePage-buttonLogin\']']
    page_content = [By.CSS_SELECTOR, 'div[class=\'StaticLoggedOutHomePage-content\']']

    # Locators - alternative static page
    login_btn_alt = [By.CSS_SELECTOR, 'a[data-testid=\'loginButton\']']
    page_content_alt = [By.CSS_SELECTOR, 'div[id=\'react-root\']']

    # Url
    path = Paths.static_logged_out_home_page

    def validate_page(self):
        """
        Validates current page
        :return: True if username input is displayed
        """
        self.soft_wait_until_visible(self.page_content)
        self.soft_wait_until_visible(self.page_content_alt)
        return self.is_visible(self.page_content) or self.is_visible(self.page_content_alt)

    def navigate_to(self):
        """
        Navigates to current page
        """
        self.navigate_to_by_url(self.url + self.path)

    def click_log_in(self):
        """
        Clicks on log in button on static logged out page
        """
        log.write_line('Clicking on Log In button on landing page')
        if self.is_visible(self.login_btn_alt, timeout=1):
            self.click(self.login_btn_alt)
        else:
            self.click(self.login_button)
