import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_NOTE = (By.CSS_SELECTOR, "button[data-testid='add-new-note']")
    TITLE = (By.ID, "title")
    DESCRIPTION = (By.ID, "description")
    SAVE = (By.CSS_SELECTOR, "button[data-testid='note-submit']")
    NOTES = (By.CSS_SELECTOR, "div[data-testid='note-card']")
    NOTE_TITLE = (By.CSS_SELECTOR, "div[data-testid='note-card-title']")
    NOTE_DELETE = (By.CSS_SELECTOR, "button[data-testid='note-delete']")
    DELETE_CONFIRM = (By.CSS_SELECTOR, "button[data-testid='note-delete-confirm']")

    def create_note(self, title, description):

        self.click(self.ADD_NOTE)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.TITLE)
        )

        self.type(self.TITLE, title)
        self.type(self.DESCRIPTION, description)

        self.click(self.SAVE)

        # Wait for save operation
        time.sleep(3)

        # Refresh because demo site updates slowly
        self.driver.refresh()

        # Wait until notes are visible again
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(self.NOTES)
        )

    def get_all_notes(self):

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(self.NOTES)
            )
        except Exception:
            return []

        return self.driver.find_elements(*self.NOTES)

    def note_card_locator_for_title(self, title):

        escaped_title = title.replace('"', '\\"')

        return (
            By.XPATH,
            f"//div[@data-testid='note-card'][.//div[@data-testid='note-card-title' and normalize-space()=\"{escaped_title}\"]]"
        )

    def wait_for_note_presence(self, title, timeout=30):

        locator = self.note_card_locator_for_title(title)

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_note_absence(self, title, timeout=30):

        locator = self.note_card_locator_for_title(title)

        def element_absent(driver):

            elems = driver.find_elements(*locator)

            return len(elems) == 0

        return WebDriverWait(self.driver, timeout).until(
            element_absent
        )

    def delete_note_by_index(self, index=0):

        notes = self.get_all_notes()

        if len(notes) <= index:
            raise IndexError(f"No note found at index {index}")

        delete_btn = notes[index].find_element(*self.NOTE_DELETE)

        self.driver.execute_script(
            "arguments[0].click();",
            delete_btn
        )

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.DELETE_CONFIRM)
        )

        self.click(self.DELETE_CONFIRM)

        time.sleep(2)

        self.driver.refresh()

    def delete_note_by_title(self, title):

        locator = self.note_card_locator_for_title(title)

        note_card = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        )

        delete_btn = note_card.find_element(*self.NOTE_DELETE)

        self.driver.execute_script(
            "arguments[0].click();",
            delete_btn
        )

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.DELETE_CONFIRM)
        )

        self.click(self.DELETE_CONFIRM)

        time.sleep(2)

        self.driver.refresh()

        self.wait_for_note_absence(title, timeout=30)

    def delete_first_note(self):

        self.delete_note_by_index(0)
    def is_note_present(self, title):

    notes = self.get_all_notes()

    return any(
        title in note.text
        for note in notes
    )
