import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome("../Driver/chromedriver_mac64") 
driver.get("https://blockchainburger.chefchain.org/") 
driver.maximize_window() 
driver.find_element_by_link_text("Check the ingredients").click()
driver.find_element_by_xpath("//h1[contains(text(),'Track all 9 ingredients')]")
print("Website is up")
time.sleep(5) 
print(driver.title) 
print(driver.current_url) 
driver.close()