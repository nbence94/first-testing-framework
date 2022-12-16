import pytest

from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import Logger
from utilities import XLUtils as xl


class Test_002_Login:

    base_url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    write_info = Logger.log_info()

    path = r".\TestData\data.xlsx"
    rows = xl.get_row_count(path, "Munka1")

    @pytest.mark.regression
    def test_login_ddt(self, setup):

        self.write_info.info("**** Test 002 / Login ****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)

        result_list = []

        for r in range(2, self.rows + 1):
            self.username = xl.read_data(self.path, "Munka1", r, 1)
            self.password = xl.read_data(self.path, "Munka1", r, 2)
            self.expectation = xl.read_data(self.path, "Munka1", r, 3)

            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            self.result_msg = "Passed"
            if act_title == exp_title:
                if self.expectation == "Good":
                    self.result_msg = "PASSED"
                    result_list.append("Passed")
                elif self.expectation == "Bad":
                    self.result_msg = "FAILED"
                    result_list.append("Failed")

                self.lp.click_logout()
                xl.write_data(self.path, "Munka1", r, 4, self.result_msg)
            elif act_title != exp_title:
                if self.expectation == "Bad":
                    result_list.append("Passed")
                    self.result_msg = "PASSED"
                elif self.expectation == "Good":
                    result_list.append("Failed")
                    self.result_msg = "FAILED"

                xl.write_data(self.path, "Munka1", r, 4, self.result_msg)

        if "Failed" not in result_list:
            self.write_info.info("**** Test is Passed ****")
            assert True
        else:
            self.write_info.info("**** Test is Failed ****")
            assert False

        self.driver.close()
