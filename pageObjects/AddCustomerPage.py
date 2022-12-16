import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customer_menu_item_xpath = "//li[@class='nav-item has-treeview menu-open']/ul/li/a[@href='/Admin/Customer/List']"
    btn_add_new_xpath = "//a[@class='btn btn-primary']"

    input_email_xpath = "//input[@id='Email']"
    input_password_xpath = "//input[@id='Password']"
    input_first_name_xpath = "//input[@id='FirstName']"
    txt_name_xpath = "//input[@id='LastName']"
    input_dob_xpath = "//input[@id='DateOfBirth']"
    input_company_name_xpath = "//input[@id='Company']"

    drop_down_customer_role_xpath = "//*[@aria-labelledby='SelectedCustomerRoleIds_label']"
    list_item_admin_xpath = "//li[contains(text(),'Administrators')]"
    list_item_registered_xpath = "//li[contains(text(),'Registered')]"
    list_item_guest_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/*[contains(text(), 'Guests')]"
    list_item_vendor_xpath = "//li[contains(text(),'Vendors')]"

    vendor_drop_down_id = "VendorId"

    input_admin_comment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customer_menu(self):
        self.driver.find_element(By.XPATH, self.customer_menu_xpath).click()

    def click_on_menu_item(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.customer_menu_item_xpath).click()

    def click_on_add_new(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_xpath).click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.input_password_xpath).send_keys(password)

    def set_customer_role(self, role):
        list = self.driver.find_elements(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li')
        if len(list) > 0:
            for i in range(len(list)):
                item = self.driver.find_element(By.XPATH,
                                                '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[@title="delete"]')
                item.click()

        self.driver.find_element(By.XPATH, self.drop_down_customer_role_xpath).click()
        time.sleep(3)

        if role == 'Registered':
            self.list_item = self.driver.find_element(By.XPATH, self.list_item_registered_xpath).click()
        elif role == 'Administrators':
            self.list_item=self.driver.find_element(By.XPATH, self.list_item_admin_xpath).click()
        elif role == 'Guests':
            self.list_item = self.driver.find_element(By.XPATH, self.list_item_guest_xpath).click()
        elif role == 'Vendors':
            self.list_item = self.driver.find_element(By.XPATH, self.list_item_vendor_xpath).click()
        else:
            self.list_item = self.driver.find_element(By.XPATH, self.list_item_guest_xpath).click()

    def set_manager_of_vendor(self, value):
        drp = Select(self.driver.find_element(By.ID, self.vendor_drop_down_id))
        drp.select_by_visible_text(value)

    def set_gender(self, gender):
        self.driver.find_element(By.XPATH, f'//*[@for="Gender_{gender}"]').click()

    def set_first_name(self, fname):
        self.driver.find_element(By.XPATH, self.input_first_name_xpath).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element(By.XPATH, self.txt_name_xpath).send_keys(lname)

    def set_dob(self, dob):
        self.driver.find_element(By.XPATH, self.input_dob_xpath).send_keys(dob)

    def set_company_name(self, comname):
        self.driver.find_element(By.XPATH, self.input_company_name_xpath).send_keys(comname)

    def set_admin_content(self, content):
        self.driver.find_element(By.XPATH, self.input_admin_comment_xpath).send_keys(content)

    def click_on_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()














