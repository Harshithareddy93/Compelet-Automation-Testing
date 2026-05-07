from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(env="local"):

    options = Options()

    options.add_argument("--start-maximized")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Local execution
    if env == "local":
        driver = webdriver.Chrome(options=options)

    # Docker / Selenium Grid execution
    elif env == "docker":
        driver = webdriver.Remote(
            command_executor="http://selenium:4444/wd/hub",
            options=options
        )

    else:
        raise ValueError("Invalid environment provided")

    driver.implicitly_wait(10)

    return driver