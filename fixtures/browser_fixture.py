from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="function")
def driver():
    options = Options()
    
    # Run in headless mode (required for Jenkins/Docker)
    options.add_argument("--headless")
    
    # Fix for Docker/Linux environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Optional but recommended (avoids crashes)
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()