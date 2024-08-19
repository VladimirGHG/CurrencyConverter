import requests
from bs4 import BeautifulSoup


class GoogleFinanceParser:
    def __init__(self, currency1, currency2, amount):
        self.site_html = requests.get(f"https://www.google.com/finance/quote/{currency1.upper()}-{currency2.upper()}",
                                      headers={
                                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}).text
        self.storage = []
        self.amount = amount

    def parseData(self):
        soup = BeautifulSoup(self.site_html, "lxml")
        exchange_rate = (soup.find("div", attrs={
            "class": "VfPpkd-WsjYwc VfPpkd-WsjYwc-OWXEXe-INsAgc KC1dQ Usd1Ac AaN0Dd  QZMA8b"}).
                         find("div", attrs={"class": "YMlKec fxKbKc"}).text)

        return exchange_rate * self.amount
