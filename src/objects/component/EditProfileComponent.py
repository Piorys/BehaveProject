
from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths


class EditProfileComponent(BaseObject.BaseObject):
    # Locators
    edit_profile_modal = [By.XPATH, '//h2[@id=\'modal-header\']/span[text()=\'Edit profile\']']
    bio_input = [By.CSS_SELECTOR, 'textarea[name=\'description\']']
    location_input = [By.CSS_SELECTOR, 'input[name=\'location\']']
    save_profile_button = [By.CSS_SELECTOR, 'div[data-testid=\'Profile_Save_Button\']']

    # Url
    path = Paths.edit_profile

    def validate_component(self):
        """
        Validates current component
        :return: True if cancel button container is visible
        """
        log.write_line('Validating components visibility')
        self.soft_wait_until_visible(self.edit_profile_modal)
        return self.is_visible(self.edit_profile_modal)

    def navigate_to(self):
        """
        Navigates to current page
        """
        self.navigate_to_by_url(self.url + self.path)

    def click_save_button(self):
        """
        Clicks on save button on edit profile modal
        """
        log.write_line('Clicking on \'Save\' button on edit profile modal')
        self.click(self.save_profile_button)

    def fill_bio(self, bio):
        """
        Fills in bio
        :param bio:
        """
        log.write_line('Filling in bio with ' + bio)
        self.wait_until_visible_and_send_keys(self.bio_input, bio)

    def fill_location(self, location):
        """
        Fills in location
        :param location:
        """
        log.write_line('Filling in location with ' + location)
        self.wait_until_visible_and_send_keys(self.location_input, location)

    def clear_bio(self):
        """
        Clears bio input
        """
        log.write_line('Clearing bio input')
        self.clear_field(self.bio_input)

    def clear_location(self):
        """
        Clears bio input
        """
        log.write_line('Clearing location input')
        self.clear_field(self.location_input)

    def wait_for_modal_to_close(self):
        """
        Waits for edit profile modal to close
        """
        log.write_line('Waiting for edit profile modal to close')
        self.wait_until_invisible(self.edit_profile_modal)
