import random

from faker import Faker
from selenium.webdriver.support.select import Select


class AddShippingHandler:
    def __init__(self, driver):
        self.driver = driver

    def add(self):
        self.driver.get('http://pmpl.frederickwilliame.com/admin/shipping/create')

        faker = Faker()
        Faker.seed()

        title_input = self.driver.find_element('id', 'inputTitle')
        title_input.clear()
        title_input.send_keys(faker.address())

        price_input = self.driver.find_element('id', 'price')
        price_input.clear()
        price_input.send_keys(random.randint(1, 1000000))

        active_dropdown = Select(self.driver.find_element('name', 'status'))
        active_dropdown.select_by_index(random.randint(0, 1))

        form = self.driver.find_element('css selector', '.card-body > form')
        form.submit()
