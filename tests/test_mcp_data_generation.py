from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from config.environment import get_config

from MCP.llm_data_generator import LLMDataGenerator


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

    initial_count = len(notes.get_all_notes())

    # MCP-generated dynamic data
    title = LLMDataGenerator.random_note_title()

    description = (
        LLMDataGenerator.random_note_description()
    )

    notes.create_note(title, description)

    # wait until note count increases
    WebDriverWait(driver, 60).until(
        lambda d: len(notes.get_all_notes()) > initial_count
    )

    final_count = len(notes.get_all_notes())

    assert final_count > initial_count