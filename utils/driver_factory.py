from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import os

load_dotenv()

def build_driver():
    options = Options()
    options.add_argument("--window-size=1400,900")

    chrome_binary = os.getenv("CHROME_BINARY")
    if not chrome_binary:
        raise RuntimeError("CHROME_BINARY не задан")
    path = Path(chrome_binary)
    if not path.exists():
        raise RuntimeError(f"chrome.exe не найден: {path}")

    options.binary_location = str(path)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    return driver
