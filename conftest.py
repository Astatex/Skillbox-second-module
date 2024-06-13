import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep


@pytest.fixture()
def set_up_browser():
    options = ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    yield driver   # до этого момента включительно выполняется преусловия, а дальше выполняется постусловия
    sleep(5)
    driver.quit()
