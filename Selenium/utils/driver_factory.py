from selenium import webdriver
from config.config import BROWSER


def create_driver():
    if BROWSER == "chrome":
        driver = webdriver.Chrome()
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    return driver
