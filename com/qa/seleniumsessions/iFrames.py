# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Properties
driver = webdriver.Chrome(executable_path="/home/mea/PycharmProjects/PythonSeleniumSessions/drivers/chromedriver")
driver.maximize_window()
driver.implicitly_wait(15)  # Waits for 10 seconds
# It waits for all elements on the page
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

# Actions
# We use switch_to.frame(name) or swithc_to.frame(id)
# Switch to frame
driver.switch_to.frame("packageListFrame")

# Click link to selenium
selenium_link = driver.find_element_by_link_text("org.openqa.selenium")
selenium_link.click()

# Switch back to the main page
driver.switch_to.default_content()

# Switch to the 2nd frame
driver.switch_to.frame("packageFrame")

# Click Web Driver
webdriver_link = driver.find_element(By.PARTIAL_LINK_TEXT, "WebDrive")
webdriver_link.click()

driver.switch_to.default_content()

# close browser
driver.close()