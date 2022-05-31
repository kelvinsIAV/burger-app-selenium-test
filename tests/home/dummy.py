import os
import unittest
from unittest.suite import TestSuite
import sys
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv

load_dotenv()

class DummyTest(unittest.TestCase):
    website_url = str(os.environ['BASE_URL'])
    webhook_url = str(os.environ['DISCORD_WEBHOOK_URL'])

    chrome_mac_driver_path = "Driver/chromedriver_mac64"
    chrome_linux_driver_path = "Driver/chromedriver_linux64"

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu') 
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(chrome_mac_driver_path, options=options) 
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(website_url) 
        driver.maximize_window() 
        
        try:
            driver.find_element(by=By.XPATH, value="//h1[contains(text(),'Track all 9 ingredients')]")
            print("Website is working")
        except:
            webhook = DiscordWebhook(url=webhook_url, content="Selenium test: " + driver.current_url)
            embed = DiscordEmbed(title='Website has problem.', description='Please Check the server', color='FF0303')
            webhook.add_embed(embed)
            response = webhook.execute()
        
        sleep(5) 
        print(driver.title) 
    finally:
        driver.close()