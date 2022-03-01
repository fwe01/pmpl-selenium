from selenium.webdriver.common.by import By


class LoginHandler:
    def __init__(self, driver, email: str, password: str):
        self.email = email
        self.driver = driver
        self.password = password

    def login(self):
        self.driver.get('http://pmpl.frederickwilliame.com/user/login')

        email_input = self.driver.find_element(By.NAME, 'email')
        email_input.clear()
        email_input.send_keys(self.email)

        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(self.password)

        login_form = self.driver.find_element(By.CSS_SELECTOR, 'form.form')
        login_form.submit()
