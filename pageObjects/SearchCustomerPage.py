from selenium.webdriver.common.by import By


class SearchCustomer:
    input_email_id = "SearchEmail"
    input_first_name_id = "SearchFirstName"
    input_last_name_id = "SearchLastName"
    btn_search_id = "search-customers"

    table_header_xpath = "//table[@role='grid']"
    table_content_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.input_email_id).clear()
        self.driver.find_element(By.ID, self.input_email_id).send_keys(email)

    def set_first_name(self, fname):
        self.driver.find_element(By.ID, self.input_first_name_id).clear()
        self.driver.find_element(By.ID, self.input_first_name_id).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element(By.ID, self.input_last_name_id).clear()
        self.driver.find_element(By.ID, self.input_last_name_id).send_keys(lname)

    def click_search(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def get_no_of_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def get_no_of_column(self):
        return len(self.driver.find_elements(By.XPATH, self.table_columns_xpath))

    def search_customer_by_email(self, email_id):
        flag = False
        for r in range(1, self.get_no_of_rows() + 1):
            email = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email == email_id:
                flag = True
                break

        return flag

    def search_customer_by_name(self, search_this):
        flag = False

        for r in range(1, self.get_no_of_rows() + 1):
            name = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == search_this:
                flag = True
                break
        return flag















