from selenium.webdriver.common.by import By

from src.objects import BaseObject
from src.helpers import Logger as log
from src.data import Paths


class TimelineComponent(BaseObject.BaseObject):
    # Locators
    timeline = [By.CSS_SELECTOR, 'div[class=\'public-DraftEditorPlaceholder-root\']']
    tweets = [By.XPATH, '//div[@data-testid=\'tweet\']/div[2]/div[2]/span']

    # Url
    path = Paths.home_page

    def validate_component(self):
        """
        Validates current component
        :return: True if editor container is visible
        """
        log.write_line('Validating components visibility')
        return self.is_visible(self.timeline)

    def navigate_to(self):
        """
        Navigates to current page
        """
        self.navigate_to_by_url(self.url + self.path)

    def is_tweet_present(self, text):
        """
        Checks if given tweet by text is present on timeline
        :text: Tweet text to search for
        """
        log.write_line('Checking if given tweet is present on timeline by text: ' + text)
        self.wait_until_visible(self.tweets)
        all_tweets = self.find_elements(self.tweets)
        for tweet in all_tweets:
            if text in tweet.text:
                log.write_line('Given tweet is present on timeline')
                return True
        log.write_line('Given tweet is not present on timeline')
        return False
