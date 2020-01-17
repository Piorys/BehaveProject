from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths


class TimelineComponent(BaseObject.BaseObject):
    # Locators
    timeline = [By.CSS_SELECTOR, 'div[class=\'public-DraftEditorPlaceholder-root\']']
    tweets = [By.XPATH, '//div[@data-testid=\'tweet\']/div[2]/div[2]/span']
    tweet_delete_button = [By.XPATH, '//div[@role=\'menu\']/div/div/div/div[@role=\'menuitem\']']

    # Url
    path = Paths.home_page

    def validate_component(self):
        """
        Validates current component
        :return: True if editor container is visible
        """
        log.write_line('Validating components visibility')
        self.soft_wait_until_visible(self.timeline)
        return self.is_visible(self.timeline)

    def navigate_to(self):
        """
        Navigates to current page
        """
        self.navigate_to_by_url(self.url + self.path)

    def format_locator_for_tweet_by_text(self, text):
        """
        Formats locator for tweet by its text
        :param text: Tweet text to search for
        """
        return [By.XPATH,
                '//div[@data-testid=\'tweet\']/div[2]/div[2]/span[text()=\''
                + text
                + '\']']

    def is_tweet_present(self, text):
        """
        Checks if given tweet by text is present on timeline
        :param text: Tweet text to search for
        """
        log.write_line('Checking if given tweet is present on timeline by text: ' + text)
        self.soft_wait_until_visible(self.tweets)
        return self.is_visible(self.format_locator_for_tweet_by_text(text))

    def click_tweet_delete_button(self):
        """
        Clicks tweet delete button, will only be visible if menu has been expanded after clicking caret
        """
        log.write_line('Clicking \'Delete\' button on tweet')
        self.click(self.tweet_delete_button)

    def click_tweet_caret_button_by_text(self,text):
        """
        Clicks on caret button on tweet found by its text
        :param text: Tweet text to search for
        """
        tweet_caret_locator = [By.XPATH,
                               '//div[@data-testid=\'tweet\']/div[2]/div[2]/span[text()=\''
                               + text
                               + '\']/../../div/div[2]/div']
        self.click(tweet_caret_locator)



