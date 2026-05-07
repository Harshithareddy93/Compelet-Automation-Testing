from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SmartWait:

    def __init__(self, driver):
        self.driver = driver

    def wait_clickable(self, locator, timeout=30):

        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_visible(self, locator, timeout=30):

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )