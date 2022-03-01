import random

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddShippingHandler:
    def __init__(self, driver):
        self.driver = driver

    def add(self):
        self.driver.get('http://pmpl.frederickwilliame.com/admin/shipping/create')

        faker = Faker()
        Faker.seed()

        title_input = self.driver.find_element(By.ID, 'inputTitle')
        title_input.clear()
        title_input.send_keys(faker.address())

        price_input = self.driver.find_element(By.ID, 'price')
        price_input.clear()
        price_input.send_keys(random.randint(1, 1000000))

        active_dropdown = Select(self.driver.find_element(By.NAME, 'status'))
        active_dropdown.select_by_index(random.randint(0, 1))

        form = self.driver.find_element(By.CSS_SELECTOR, '.card-body > form')
        form.submit()
