import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/home/mea/PycharmProjects/PythonSeleniumSessions/drivers/chromedriver")
# For Chrome

driver.maximize_window()  # Maximizes the window size
driver.implicitly_wait(10)

# driver = webdriver.Firefox(executable_path="/home/mea/PycharmProjects/PythonSeleniumSessions/drivers/geckodriver")
# For Firefox

driver.get("https://jobs.workable.com/")  # Launches application in test

time.sleep(5)

title = driver.title  # gets title of the page
print(title)  # Prints the title

url = driver.current_url  # gets current URL
print(url)

page_source = driver.page_source  # Returns the HTML code of the page
# print(page_source)

driver.find_element_by_link_text("Retail Sales Executive - Cosmetics/Haircare").click()


driver.close()  # Closes one browser at a time

# driver.quit()  # It will close all the browsers
