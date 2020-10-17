# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Properties
driver = webdriver.Chrome(executable_path="/home/mea/PycharmProjects/PythonSeleniumSessions/drivers/chromedriver")
driver.maximize_window()
driver.implicitly_wait(15)  # Waits for 10 seconds
# It waits for all elements on the page
driver.get("https://www.seleniumeasy.com/test/")

# Actions
alert_link = driver.find_element_by_link_text("Alerts & Modals")
alert_link.click()

window_pop_up = driver.find_element_by_link_text("Javascript Alerts")
window_pop_up.click()

click_me_btn = driver.find_element_by_xpath("//button[contains(text(),'Click me!')]")
click_me_btn.click()

driver.switch_to.alert.accept()  # Closes alert window using ok button
# driver.switch_to.alert.dismiss() # Close alert with cancel button

# close active window
driver.close()
