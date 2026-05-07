from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(env="local"):

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if env == "grid":
        driver = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            options=options
        )
    else:
        driver = webdriver.Chrome(options=options)

    return driver