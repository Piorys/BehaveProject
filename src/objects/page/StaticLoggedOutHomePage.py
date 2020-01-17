from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths

class StaticLoggedOutHomeObject(BaseObject.BaseObject):

    # Locators
    login_button = [By.CSS_SELECTOR, 'a[class*=\'StaticLoggedOutHomePage-buttonLogin\']']
    page_content = [By.CSS_SELECTOR, 'div[class=\'StaticLoggedOutHomePage-content\']']

    # Url
    path = Paths.static_logged_out_home_page

    def validate_page(self):
        """
        Validates current page
        :return: True if username input is displayed
        """
        self.soft_wait_until_visible(self.page_content)
        return self.is_visible(self.page_content)

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
        self.click(self.login_button)
