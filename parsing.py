from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def selenium_parser(trading_pair):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Sergiy\\Desktop\\superlabs test\\superlabs\\chromedriver.exe",
        options=options
    )
    try:
        driver.get("https://paper-trader.frwd.one/")
        time.sleep(3)
        input_trading_pair = driver.find_element(By.XPATH, "/html/body/form/input[1]")
        input_trading_pair.clear()
        input_trading_pair.send_keys(trading_pair)

        input_timeframe = driver.find_element(By.XPATH, "/html/body/form/input[2]")
        input_timeframe.clear()
        input_timeframe.send_keys("5m")

        input_count_of_candles = driver.find_element(By.XPATH, "/html/body/form/input[3]")
        input_count_of_candles.clear()
        input_count_of_candles.send_keys("999")

        input_period_of_MA = driver.find_element(By.XPATH, "/html/body/form/input[4]")
        input_period_of_MA.clear()
        input_period_of_MA.send_keys("25")

        input_profit_percentage = driver.find_element(By.XPATH, "/html/body/form/input[5]")
        input_profit_percentage.clear()
        input_profit_percentage.send_keys("10")

        input_loss_percentage = driver.find_element(By.XPATH, "/html/body/form/input[6]")
        input_loss_percentage.clear()
        input_loss_percentage.send_keys("1")

        calculate = driver.find_element(By.XPATH,"/html/body/form/input[7]")
        calculate.click()

        image = driver.find_element(By.XPATH, "/html/body/img")
        print(image)

        time.sleep(10)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()