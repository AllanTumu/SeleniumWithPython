from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/home/mea/PycharmProjects/PythonSeleniumSessions/drivers/chromedriver")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.seleniumeasy.com/test/")
print(driver.title)

driver.get("https://www.pavantestingtools.com/")
print(driver.title)

driver.back() # Goes back

print(driver.title)

driver.forward() # Goes Forward

print(driver.title)

driver.close()
