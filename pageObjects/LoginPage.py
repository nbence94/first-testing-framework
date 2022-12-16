from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//*[@class='button-1 login-button']"
    link_logout_xpath = "//*[@href='/logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        user_input = self.driver.find_element(By.ID, self.textbox_username_id)
        user_input.clear()
        user_input.send_keys(username)

    def set_password(self, password):
        password_input = self.driver.find_element(By.ID, self.textbox_password_id)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(By.XPATH, self.button_login_xpath)
        login_button.click()

    def click_logout(self):
        logout_button = self.driver.find_element(By.XPATH, self.link_logout_xpath)
        logout_button.click()

