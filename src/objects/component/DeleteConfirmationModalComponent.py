from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths


class DeleteConfirmationModalComponent(BaseObject.BaseObject):
    # Locators
    cancel_button = [By.XPATH, '//span[text()=\'Delete\']']
    delete_button = [By.CSS_SELECTOR, 'div[data-testid=\'confirmationSheetConfirm\']']

    # Url
    path = Paths.home_page

    def validate_component(self):
        """
        Validates current component
        :return: True if cancel button container is visible
        """
        log.write_line('Validating components visibility')
        self.soft_wait_until_visible(self.cancel_button)
        return self.is_visible(self.cancel_button)

    def navigate_to(self):
        """
        Navigates to current page
        """
        self.navigate_to_by_url(self.url + self.path)

    def click_delete_button(self):
        """
        Clicks on delete button on delete confirmation modal
        """
        log.write_line('Clicking on \'delete\' button on delete confirmation modal')
        self.click(self.delete_button)
