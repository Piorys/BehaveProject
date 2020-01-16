from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from src.config import TestConf


class BasePage(object):
    """ Page objects are to inherit from BasePage """

    url = ""
    driver = TestConf.driver

    def wait_until_visible(self, locator, timeout=TestConf.timeout):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator, timeout=TestConf.timeout):
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def is_visible(self, locator, timeout=1):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
