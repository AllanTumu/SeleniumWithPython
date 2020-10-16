from selenium import webdriver
driver = webdriver.Chrome("/home/mea/PycharmProjects/PythonSeleniumSessions/drivers/chromedriver")
driver.get("https://freecrm.com/")
driver.maximize_window()

driver.implicitly_wait(1000)

title = driver.title

driver.find_element_by_xpath("//a[contains(text(),'Compare')]").click()

print(title)

assert "#1 Free CRM customer relationship management software cloud" in title

driver.quit()
