from selenium import webdriver
from bs4 import BeautifulSoup

def selenium_parser(trading_pair):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Sergiy\\Desktop\\superlabs test\\superlabs\\chromedriver.exe",
        options=options
    )
    try:
        pass
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()