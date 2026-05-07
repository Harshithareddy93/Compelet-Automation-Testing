from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.environment import get_config
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_empty_note_validation(driver):
    config = get_config()

    driver.get(config["base_url"])

    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    login = LoginPage(driver)
    login.login(config["email"], config["password"])

    notes = ProductPage(driver)

    notes.click(notes.ADD_NOTE)

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(notes.TITLE)
    )

    notes.click(notes.SAVE)

    title_error = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'invalid-feedback') and normalize-space(text())='Title is required']"
            )
        )
    )

    desc_error = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'invalid-feedback') and normalize-space(text())='Description is required']"
            )
        )
    )

    assert title_error.is_displayed()
    assert desc_error.is_displayed()