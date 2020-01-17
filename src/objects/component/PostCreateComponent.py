from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths
from src.config import TestConf

class PostCreateComponent(BaseObject.BaseObject):
    # Locators
    editor_container = [By.CSS_SELECTOR, 'div[class=\'public-DraftEditorPlaceholder-root\']']
    editor_input = [By.CSS_SELECTOR, 'div[class*=\'public-DraftEditor-content\'][role=\'textbox\']']

    # Url
    path = Paths.home_page

    def validate_component(self):
        """
        Validates current component
        :return: True if editor container is visible
        """
        log.write_line('Validating components visibility')
        return self.is_visible(self.editor_container)

    def navigate_to(self):
        """
        Navigates to current page
        """
        self.navigate_to_by_url(self.url + self.path)

    def fill_editor(self, text):
        """
        Fills in post create editor
        """
        log.write_line('Filling in post create editor with ' + text)
