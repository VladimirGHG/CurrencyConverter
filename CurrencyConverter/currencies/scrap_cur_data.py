from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class GoogleFinanceParser:
    def __init__(self, currency1, currency2, amount):
        driver = webdriver.Chrome()

        self.js_content = driver.page_source
        self.amount = amount
        self.currency1 = currency1
        self.currency2 = currency2

    def parseData(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless if you don't need a visible browser window
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Set up the WebDriver
        service = Service("C:/Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            driver.get(f"https://www.google.com/finance/quote/{self.currency1.upper()}-{self.currency2.upper()}")

            driver.implicitly_wait(15)  # seconds

            exchange_rate_element = driver.find_element(By.CLASS_NAME, 'YMlKec.fxKbKc')

            exchange_rate = float(exchange_rate_element.text)

        finally:
            driver.quit()

        return [exchange_rate * self.amount, exchange_rate]

