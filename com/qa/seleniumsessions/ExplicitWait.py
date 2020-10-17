# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Properties
driver = webdriver.Chrome(executable_path="/home/mea/PycharmProjects/PythonSeleniumSessions/drivers/chromedriver")
driver.maximize_window() # Maximizes window
driver.implicitly_wait(10)  # Waits for 10 seconds
# It waits for all elements on the page
driver.get("https://www.expedia.com")


