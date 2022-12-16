import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.read_properties import ReadConfig
from utilities.custom_logger import Logger
import string
import random


class Test_003_AddCustomer:

    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = Logger.log_info()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.add_customer = AddCustomer(self.driver)
        self.add_customer.click_on_customer_menu()
        self.add_customer.click_on_menu_item()

        self.add_customer.click_on_add_new()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@email.com"
        self.add_customer.set_email(self.email)
        self.add_customer.set_password("test123")
        self.add_customer.set_first_name("Test")
        self.add_customer.set_last_name("James")
        self.add_customer.set_gender("Male")
        self.add_customer.set_dob("7/05/1985")  # Format: D / MM / YYY
        self.add_customer.set_company_name("busyQA")

        self.add_customer.set_customer_role("Guests")
        self.add_customer.set_manager_of_vendor("Vendor 2")

        time.sleep(3)
        self.add_customer.set_admin_content("This is for testing.........")
        self.add_customer.click_on_save()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(r".\Screenshots\test_addCustomer_scr.png")
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))



















