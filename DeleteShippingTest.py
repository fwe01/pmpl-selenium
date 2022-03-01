from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Handler.DeleteShippingHandler import DeleteShippingHandler
from Handler.LoginHandler import LoginHandler

if __name__ == '__main__':
    driver = webdriver.Firefox()

    # Login
    loginHandler = LoginHandler(driver, 'admin@gmail.com', '1111')
    loginHandler.login()

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.alert.alert-success')))

    deleteShipping = DeleteShippingHandler(driver)
    deleteShipping.delete()

    # Logout
    # logoutHandler = LogoutHandler(driver)
    # logoutHandler.logout()
