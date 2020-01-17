from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths


class NavigationBarComponent(BaseObject.BaseObject):
    # Locators
    nav_bar = [By.CSS_SELECTOR, 'nav[role=\'navigation\'][aria-label=\'Primary\']']
    profile_link = [By.CSS_SELECTOR, 'a[aria-label=\'Profile\']']

    # Url
    path = Paths.home_page

    def validate_component(self):
        """
        Validates current component
        :return: True if cancel button container is visible
        """
        log.write_line('Validating components visibility')
        self.soft_wait_until_visible(self.nav_bar)
        return self.is_visible(self.nav_bar)

    def navigate_to(self):
        """
        Navigates to current page
        """
        self.navigate_to_by_url(self.url + self.path)

    def click_profile_button(self):
        """
        Clicks on profile buton on left hand navigation bar
        """
        log.write_line('Clicking on \'Profile\' button on left hand navigation bar')
        self.click(self.profile_link)
