import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.read_properties import ReadConfig
from utilities.custom_logger import Logger


class Test_SearchCustomerByName_004:
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = Logger.log_info()  # Logger

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.logger.info("************* SearchCustomerByName_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        # Navigate to the Menu
        self.add_cust = AddCustomer(self.driver)
        self.add_cust.click_on_customer_menu()
        self.add_cust.click_on_menu_item()
        time.sleep(2)

        # Searching
        search_cust = SearchCustomer(self.driver)
        search_cust.set_first_name("Victoria")
        search_cust.set_last_name("Terces")
        search_cust.click_search()
        time.sleep(5)
        status = search_cust.search_customer_by_name("Victoria Terces")
        self.driver.close()

        if status:
            self.logger.info("***************  SearchCustomerByName_004 PASSED  *********** ")
            assert True
        else:
            self.logger.info("***************  SearchCustomerByName_004 FAILED  *********** ")
            assert False













