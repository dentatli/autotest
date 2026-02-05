from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import settings

def build_driver():
    options = Options()

    if settings.chrome_binary:
        options.binary_location = settings.chrome_binary

    if settings.headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver
