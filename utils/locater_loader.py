from selenium.webdriver.common.by import By


class LocatorLoader:

    LOCATORS = {

        "login_email": [
            (By.NAME, "email"),
            (By.ID, "email"),
            (By.XPATH, "//input[@type='email']")
        ],

        "login_password": [
            (By.NAME, "password"),
            (By.ID, "password"),
            (By.XPATH, "//input[@type='password']")
        ],

        "login_button": [
            (By.XPATH, "//button[contains(text(),'Login')]"),
            (By.CSS_SELECTOR, "button[type='submit']"),
            (By.ID, "loginBtn")
        ],

        "add_note_button": [
            (By.XPATH, "//button[contains(text(),'Add Note')]"),
            (By.CSS_SELECTOR, "button.btn")
        ],

        "note_title": [
            (By.NAME, "title"),
            (By.ID, "title")
        ],

        "note_description": [
            (By.NAME, "description"),
            (By.ID, "description")
        ],

        "save_button": [
            (By.XPATH, "//button[contains(text(),'Save')]"),
            (By.CSS_SELECTOR, "button[type='submit']")
        ]
    }

    @classmethod
    def get_locator(cls, locator_name):

        return cls.LOCATORS.get(locator_name, [])