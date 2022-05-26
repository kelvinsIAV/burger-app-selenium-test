import os
import unittest
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

webhook_url = "https://discord.com/api/webhooks/841577243751088148/0aiGgeGATYNaG0hj-dFo5chxwp3Avrfq1Xj46-G_MLICX2gm_ROTKmPip8oCzuaL3YUd"

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
    driver.get("https://consumer.burgerchain.stg.thenewfork.com") 
    driver.maximize_window() 
    try:
        driver.find_element(by=By.XPATH, value="//h1[contains(text(),'Track all 9 ingredients')]")
        print("Website is working")
    except:
        webhook = DiscordWebhook(url=webhook_url, content="Selenium test: " + driver.current_url)
        # create embed object for webhook
        # you can set the color as a decimal (color=242424) or hex (color='03b2f8') number
        embed = DiscordEmbed(title='Website has problem.', description='Please Check the server', color='FF0303')

        # add embed object to webhook
        webhook.add_embed(embed)

        response = webhook.execute()
    
    sleep(5) 
    print(driver.title) 
finally:
    driver.close()