from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.config_reader import get_config
from utils.llm_data_generator import LLMDataGenerator


def test_mcp_dynamic_note_creation(driver):

    config = get_config()

    driver.get(config["base_url"])

    WebDriverWait(driver, 60).until(
        lambda d: d.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    login = LoginPage(driver)

    login.login(
        config["email"],
        config["password"]
    )

    notes = ProductPage(driver)

    # MCP-generated dynamic data
    title = LLMDataGenerator.random_note_title()

    description = (
        LLMDataGenerator.random_note_description()
    )

    notes.create_note(title, description)

    # refresh page to get latest notes
    driver.refresh()

    # wait until created note appears
    WebDriverWait(driver, 60).until(
        lambda d: notes.is_note_present(title)
    )

    assert notes.is_note_present(title)
