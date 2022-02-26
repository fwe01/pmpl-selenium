from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Handler.LoginHandler import LoginHandler

driver = webdriver.Firefox()

# driver.get('http://pmpl.frederickwilliame.com')

# Login
loginHandler = LoginHandler(driver, 'admin@gmail.com', '1111')
loginHandler.login()

# Logout
# logoutHandler = LogoutHandler(driver)
# logoutHandler.logout()

