from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from src.config import TestConf


class BaseObject(object):
    """ Page objects are to inherit from BasePage """

    driver = TestConf.driver
    url = TestConf.env

    def __init__(self):
        pass

    def find_element(self, locator):
        return self.driver.find_element(locator[0], locator[1])

    def wait_until_visible(self, locator, timeout=TestConf.timeout):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((locator[0], locator[1])))

    def wait_until_clickable(self, locator, timeout=TestConf.timeout):
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable((locator[0], locator[1])))

    def wait_until_visible_and_send_keys(self, locator, keys):
        self.wait_until_visible(locator)
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(keys)

    def navigate_to_by_url(self, url):
        self.driver.get(url)

    def is_visible(self, locator, timeout=TestConf.timeout):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click(self, locator):
        self.wait_until_visible(locator)
        self.wait_until_clickable(locator)
        self.find_element(locator).click()
