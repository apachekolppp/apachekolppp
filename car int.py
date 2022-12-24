#import the necessary packages
from selenium import webdriver

#create a webdriver instance
driver = webdriver.Chrome()

#navigate to the Snapchat login page
driver.get("https://accounts.snapchat.com/accounts/login")

#enter the username and password
username_field = driver.find_element_by_name("rcc8i")
username_field.send_keys("rcc8i")
