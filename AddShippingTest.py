from Handler.AddShippingHandler import AddShippingHandler
from Handler.LoginHandler import LoginHandler
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Handler.LoginHandler import LoginHandler

if __name__ == '__main__':
    driver = webdriver.Firefox()
    loginHandler = LoginHandler(driver, 'admin@gmail.com', '1111')
    loginHandler.login()

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located(('css selector', '.alert.alert-success')))

    addShippingHandler = AddShippingHandler(driver)
    addShippingHandler.add()
