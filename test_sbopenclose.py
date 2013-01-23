from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

from elements import *
import login

class TestSbopenclose(unittest.TestCase):
    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        desired_capabilities['version'] = '9'
        desired_capabilities['platform'] = 'Windows 2008'
        desired_capabilities['name'] = 'Test of S&B "friends" button, IE9 and Window2008'
        desired_capabilities['command-timeout'] = 40
        desired_capabilities['idle-timeout'] = 60

        self.driver = webdriver.Remote(
                                       desired_capabilities=desired_capabilities, 
                                       command_executor="http://bschael:63bd1368-87eb-41a6-a2a8-d668b71a5997@ondemand.saucelabs.com:80/wd/hub"
                                       )
        self.driver.implicitly_wait(10)
        self.base_url = URL.url_eshopbuild
        self.verificationErrors = []
    
    def test_sbopenclose(self):
        driver = self.driver
        driver.get(URL.url_fb)
        driver.delete_all_cookies()
        
        driver.get(self.base_url)
        
        for i in range(60):
            try:
                if self.is_element_present(By.ID, EShop.ribbon): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id(EShop.ribbon).click()
        time.sleep(10)
        for i in range(60):
            try:
                if self.is_element_present(By.ID, EShop.start_fb_button): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.assertTrue(self.is_element_present(By.ID, EShop.start_fb_button))
        driver.find_element_by_id(EShop.start_fb_button).click()
        
         # Change to FB PopUp
        time.sleep(10) 
        login.FB_Login(driver, FBUsers.ie_user1, FBLogin.fb_password)

        for i in range(60):
            try:
                if self.is_element_present(By.ID, EShop.hide_sb_pannel_online): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id(EShop.hide_sb_pannel_online).click()
        time.sleep(10)
        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
