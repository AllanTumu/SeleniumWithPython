# Imports
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Properties
driver = webdriver.Chrome(executable_path="/home/mea/PycharmProjects/PythonSeleniumSessions/drivers/chromedriver")
driver.maximize_window()
driver.implicitly_wait(15)  # Waits for 10 seconds
# It waits for all elements on the page
driver.get("http://automationpractice.com/index.php")

# Actions
# Capture the elements
signin_btn = driver.find_element_by_xpath("//a[contains(text(),'Sign in')]")

# Check if heading is displayed
print(signin_btn.is_displayed())
print(signin_btn.is_enabled())

# Click the signin button to create account
signin_btn.click()

# Enter email
email_txt_box = driver.find_element_by_xpath("//input[@id='email_create']")
email_txt_box.send_keys("mbonye@gmail.com")

# Click the Create Account button
create_account_btn = driver.find_element_by_xpath("//button[@id='SubmitCreate']")
create_account_btn.click()

# Fill form
gender_checkbox = driver.find_element_by_xpath("//input[@id='id_gender1']")
gender_checkbox.click()

first_name = driver.find_element_by_xpath("//input[@id='customer_firstname']")
first_name.send_keys("Mbonyebyombii")

last_name = driver.find_element_by_xpath("//input[@id='customer_lastname']")
last_name.send_keys("The Great")

password = driver.find_element_by_xpath("//input[@id='passwd']")
password.send_keys("12345678")

# Select from drop down
day_of_birth = driver.find_element_by_xpath("//select[@id='days']")
day_of_birth = Select(driver.find_element_by_xpath("//select[@id='days']"))
day_of_birth.select_by_value('10')

# Count Number of options
day_of_birth_options = day_of_birth.options
# for i in day_of_birth_options:
#    print(i.text)

print(len(day_of_birth.options))

month_of_birth = Select(driver.find_element_by_xpath("//select[@id='months']"))
month_of_birth.select_by_value('7')
# month_of_birth.select_by_index(7)

year_of_birth = Select(driver.find_element_by_xpath("//select[@id='years']"))
year_of_birth.select_by_value('1998')

# How to find the value of text boxes on a page
input_boxes = driver.find_elements(By.CLASS_NAME, 'form-control')
print(len(input_boxes))

# find links
links = driver.find_elements(By.TAG_NAME, 'a')
print("Number of links is :", len(links))
for num_links in links:
    print(num_links.text)

# Clicking links
click_specials = driver.find_element(By.PARTIAL_LINK_TEXT, "Special")
click_specials.click()

# Working with Alerts and Pop ups
#
# Exit the browser
driver.close()
