from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths


class ProfilePage(BaseObject.BaseObject):

    # Locators
    edit_profile_button = [By.CSS_SELECTOR, 'a[href=\'/settings/profile\']']
    bio_field = [By.XPATH, '//div[@data-testid=\'UserDescription\']/span']
    location_field = [By.XPATH, '//div[@data-testid=\'UserProfileHeader_Items\']/span/span/span']

    # Url
    path = Paths.profile_page

    def validate_page(self):
        """
        Validates current page
        :return: True if username input is displayed
        """
        self.soft_wait_until_visible(self.edit_profile_button)
        return self.is_visible(self.edit_profile_button)

    def navigate_to(self):
        """
        Navigates to current page
        """
        self.navigate_to_by_url(self.url+self.path)

    def click_edit_profile(self):
        """
        Clicks on Edit Profile button
        """
        log.write_line('Clicking on edit profile button')
        self.click(self.edit_profile_button)

    def get_profile_bio(self):
        """
        Retrieves user bio from profile page
        :return: - Bio
        """
        log.write_line('Retrieving bio from profile page')
        self.wait_until_visible(self.bio_field)
        return self.find_element(self.bio_field).text

    def get_profile_location(self):
        """
        Retrieves user location from profile page
        :return: - location
        """
        log.write_line('Retrieving location from profile page')
        self.wait_until_visible(self.location_field)
        return self.find_element(self.location_field).text
