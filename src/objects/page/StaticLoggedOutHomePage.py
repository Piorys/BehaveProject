from selenium.webdriver.common.by import By
from src.objects.page import BasePage
from src.helpers import Logger as log


class StaticLoggedOutHomePage(BasePage.BasePage):

    # Locators
    login_button = [By.CSS_SELECTOR, 'a[class*=\'StaticLoggedOutHomePage-buttonLogin\']']
    page_content = [By.CSS_SELECTOR, 'div[class=\'StaticLoggedOutHomePage-content\']']

    # Url
    url = ''

    def validate_page(self):
        """
        Validates current page
        :return: True if username input is displayed
        """
        return self.is_visible(self.page_content)

    def navigate_to(self):
        """
        Navigates to current page
        """

    def click_log_in(self):
        """
        Clicks on log in button on static logged out page
        """
        log.write_line('Clicking on Log In button on landing page')
        self.click(self.login_button)
