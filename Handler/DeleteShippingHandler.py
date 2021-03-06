import random

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class DeleteShippingHandler:
    driver: WebDriver

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def delete(self):
        self.driver.get('http://pmpl.frederickwilliame.com/admin/shipping/')

        shipping_delete_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'form > button.dltBtn')

        shipping_delete_button = shipping_delete_buttons[random.randint(0, len(shipping_delete_buttons) - 1)]
        shipping_delete_button.click()

        confirm_button = self.driver.find_element(By.CSS_SELECTOR, '.swal-button-container > .swal-button--confirm')
        confirm_button.click()
