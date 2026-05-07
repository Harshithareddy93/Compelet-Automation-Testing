import pytest
from utils.driver_factory import get_driver

@pytest.fixture(scope="function")
def driver():

    driver = get_driver(env="docker")

    yield driver

    driver.quit()