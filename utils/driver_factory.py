import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Hide webdriver-manager logs
os.environ["WDM_LOG"] = "0"


BASE_URL = "https://practice.expandtesting.com/notes/app"


def get_driver(env="grid"):

    chrome_options = Options()

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    # Hide browser logs
    chrome_options.add_experimental_option(
        "excludeSwitches",
        ["enable-logging"]
    )

    chrome_options.add_experimental_option(
        "useAutomationExtension",
        False
    )

    if env == "grid":

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=chrome_options
        )

    else:

        service = Service(
            ChromeDriverManager().install()
        )

        service.creationflags = 0x08000000

        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )


    driver.get(BASE_URL)

    return driver