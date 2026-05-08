from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from config.environment import get_config

from MCP.llm_data_generator import LLMDataGenerator


def test_mcp_invalid_login(driver):

    config = get_config()

    driver.get(config["base_url"])
    
    WebDriverWait(driver, 80).until(
        lambda d: d.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    login = LoginPage(driver)

    # MCP-generated invalid credentials
    random_email = (
        LLMDataGenerator.random_email()
    )

    random_password = "InvalidPassword123"

    # perform invalid login
    login.login(
        random_email,
        random_password
    )

    # verify login failed
    WebDriverWait(driver, 5).until(
        lambda d: True
    )

    assert "login" in driver.current_url.lower()