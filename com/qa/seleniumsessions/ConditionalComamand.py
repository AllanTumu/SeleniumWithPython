# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Properties
driver = webdriver.Chrome(executable_path="/home/mea/PycharmProjects/PythonSeleniumSessions/drivers/chromedriver")
driver.maximize_window()
driver.implicitly_wait(10)  # Waits for 10 seconds
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

day_of_birth = driver.find_element_by_xpath("//select[@id='days']")
day_of_birth.click()

# Exit the browser
# driver.close()
