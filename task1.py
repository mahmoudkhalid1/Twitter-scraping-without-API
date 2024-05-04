from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
from selenium.webdriver.common.by import By

# Initialize Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background
driver = webdriver.Chrome(options=chrome_options)

def scrape_twitter_for_stock_symbol(accounts, stock_symbol, interval_minutes):
    stock_symbol_pattern = re.compile(r'\$' + stock_symbol + r'\b', re.IGNORECASE)
    results = {}

    for account in accounts:
        driver.get(account)
        sleep(5)  # Wait for the page to load

        # Scroll to load more tweets. Adjust the range for more scrolling (more tweets).
        for _ in range(5):  # Adjust the range as needed
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            sleep(3)

        page_source = driver.page_source
        mentions = len(stock_symbol_pattern.findall(page_source))
        results[account] = mentions

    return results

# Example usage
twitter_accounts = [
    "https://twitter.com/Mr_Derivatives",
    "https://twitter.com/warrior_0719",
    "https://twitter.com/ChartingProdigy",
    "https://twitter.com/allstarcharts",
    "https://twitter.com/yuriymatso",
    "https://twitter.com/TriggerTrades",
    "https://twitter.com/AdamMancini4",
    "https://twitter.com/CordovaTrades",
    "https://twitter.com/Barchart",
    "https://twitter.com/RoyLMattox"
    # Add the rest of the accounts
]
stock_symbol = "AAPL"  # Example stock symbol
interval_minutes = 15  # Example interval
while True:
    results = scrape_twitter_for_stock_symbol(twitter_accounts, stock_symbol, interval_minutes)
    for account, mentions in results.items():
        print(f"'${stock_symbol}' was mentioned '{mentions}' times in '{account}' in the last '{interval_minutes}' minutes.")
    sleep(15*60)

driver.quit()