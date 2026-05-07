import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():

    options = Options()

    # Headless mode for Jenkins
    options.add_argument("--headless=new")

    # Required for Docker/Jenkins
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Optional stability settings
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Create Chrome driver
    driver = webdriver.Chrome(options=options)

    # Maximize window
    driver.maximize_window()

    yield driver

    # Close browser after test
    driver.quit()