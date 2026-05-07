from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(env="local"):

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new")

    if env == "docker":
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )

    else:
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    return driver