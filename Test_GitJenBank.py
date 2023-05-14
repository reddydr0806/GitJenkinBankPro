from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

class Test_BankProjectDemo():
    def Test_BankLogin(self):
        driver.get("https://parabank.parasoft.com/parabank/index.htm")
        driver.maximize_window()
        time.sleep(3)

#Registration

        click_register = driver.find_element(By.XPATH, "//*[contains(text(), 'Register')]").click()
# click_register = driver.find_element(By.XPATH, "//*[contains(text(), 'rgstr')]").click()
        time.sleep(3)

#fill details for Registrations

        first_name = driver.find_element(By.XPATH, "//input[@id='customer.firstName']").send_keys('Shiva')
        last_name = driver.find_element(By.XPATH, "//input[@id='customer.lastName']").send_keys('test')
        address_detail = driver.find_element(By.XPATH, '//input[@id="customer.address.street"]').send_keys('1234 Street')
        city_detail = driver.find_element(By.XPATH, '//input[@id="customer.address.city"]').send_keys('Delhi')
        state_detail = driver.find_element(By.XPATH, '//input[@id="customer.address.state"]').send_keys('New Delhi')
        ZipCode_detial = driver.find_element(By.XPATH, '//input[@id="customer.address.zipCode"]').send_keys('55123')
        phone_detail = driver.find_element(By.XPATH, '//input[@id="customer.phoneNumber"]').send_keys('9886320044')
        ssn_detail = driver.find_element(By.XPATH, '//input[@id="customer.ssn"]').send_keys('039-88-9654')

        username_detial = driver.find_element(By.XPATH, '//input[@id="customer.username"]').send_keys('danatest111')
        password_detial = driver.find_element(By.XPATH, '//input[@id="customer.password"]').send_keys('test@123')
        confirm_password = driver.find_element(By.XPATH, '//input[@id="repeatedPassword"]').send_keys('test@123')

        submit_register = driver.find_element(By.XPATH, '//input[@value="Register"]').click()
        time.sleep(3)

#log out the Account details page

        logout_page = driver.find_element(By.XPATH, "//*[contains(text(), 'Log Out')]").click()
        print("Bank Login & Logout was successful")

#call the Class & Function
BankLogin1 = Test_BankProjectDemo()
BankLogin1.Test_BankLogin()

print(driver.title)
driver.quit()