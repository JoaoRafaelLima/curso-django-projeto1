from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# CASO fosse do jeito do selanium antigo:

# from pathlib import Path

# ROOT_PATH = Path(__file__).parent.parent
# CHROMEDRIVER_NAME = "chromedriver.exe"
# CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME

def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    servico = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=servico, options=chrome_options)
    return browser

if __name__ == "__main__":
    broswer = make_chrome_browser('--headless')
    broswer.get("https://www.google.com/")
    broswer.quit()