import pytest

from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import Logger


class Test_001_Login:

    base_url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    write_info = Logger.log_info()

    @pytest.mark.regression
    def test_home_page_title(self, setup):

        self.write_info.info("**** Test 001 / Title ****")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.driver.close()
            self.write_info.info("**** Title Test - Passed ****")
            assert True
        else:
            self.write_info.info("**** Title Test - Failed ****")
            self.driver.save_screenshot(r".\Screenshots\screen_problem.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.write_info.info("**** Test 001 / Login ****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.write_info.info("**** Login Test - Passed ****")
            self.lp.click_logout()
            self.driver.close()
            assert True
        else:
            self.write_info.info("**** Login Test - Failed ****")
            self.driver.save_screenshot(r".\Screenshots\login_problem.png")
            self.driver.close()
            assert False
