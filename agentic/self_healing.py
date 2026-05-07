from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SelfHealingDriver:

    def __init__(self, driver):
        self.driver = driver

    def find_element_heal(self, locators, timeout=20):

        for by, value in locators:

            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, value))
                )

                print(f"[HEALED] Locator worked: {value}")

                return element

            except:
                continue

        raise Exception("All locators failed")