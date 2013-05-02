from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys

from elements import *


class Browser:
    
    IPHONE    = 0
    IPAD      = 1
    ANDROID   = 2
class TestUser:
    
    version              = ''
    test_name            = ''
    
    email_user_one       = ''
    username_one         = ''
    id_user_one          = ''
    name_user_one        = ''
    full_name_user_one   = ''
    email_user_two       = ''
    username_two         = ''
    id_user_two          = ''
    name_user_two        = ''
    full_name_user_two   = ''
    email_user_three     = ''
    username_three       = ''
    id_user_three        = ''
    name_user_three      = ''
    full_name_user_three = ''
    password             = ''
    email_link           = ''
    browser              = None
    desired_capabilities = []
    browser_type         = None
    
    def __init__(self, version, test_name, email_user_one, username_one, id_user_one, name_user_one, full_name_user_one, email_user_two, username_two, id_user_two, name_user_two, full_name_user_two, email_user_three, username_three, id_user_three, name_user_three, full_name_user_three, password, email_link, browser_type):
        
        self.version              = version
        self.test_name            = test_name
        self.email_user_one       = email_user_one
        self.username_one         = username_one
        self.id_user_one          = id_user_one
        self.name_user_one        = name_user_one
        self.full_name_user_one   = full_name_user_one
        self.email_user_two       = email_user_two
        self.username_two         = username_two
        self.id_user_two          = id_user_two
        self.name_user_two        = name_user_two
        self.full_name_user_two   = full_name_user_two
        self.email_user_three     = email_user_three
        self.username_three       = username_three
        self.id_user_three        = id_user_three
        self.name_user_three      = name_user_three
        self.full_name_user_three = full_name_user_three
        self.password             = password
        self.email_link           = email_link
        self.browser_type         = browser_type
        print "init ready"
        
        self.desired_capabilities = self.get_desired_capabilities()
        
    def get_desired_capabilities(self):
        
        desired_capabilities = []
        
        def desired_capability_base():
            """ Returns the base of any desired capabilty
            """
            cap_obj = {'javascriptEnabled': True}
            cap_obj['version'] = ''
            cap_obj['platform'] = 'ANY'
            cap_obj['command-timeout'] = 40
            cap_obj['idle-timeout'] = 60
            cap_obj['max-duration']    = 150

            if self.browser_type == Browser.IPHONE:
                cap_obj['browserName'] = 'iphone'
                cap_obj['name'] = self.test_name+' iPhone'
            elif self.browser_type == Browser.IPAD:
                cap_obj['name'] = self.test_name+' iPad'
                cap_obj['browserName'] = 'ipad'
            elif self.browser_type == Browser.ANDROID:
                cap_obj['browserName'] = 'android'
                cap_obj['name'] = self.test_name+' Android'

            return cap_obj


        if self.browser_type == Browser.IPHONE:
            desired_capability = desired_capability_base()
            desired_capability['version']    = '6'
            desired_capability['platform']   = 'OS X 10.8'
            desired_capabilities.append(desired_capability)
            
        elif self.browser_type == Browser.IPAD:
            desired_capability = desired_capability_base()
            desired_capability['version']    = '5.1'
            desired_capability['platform']   = 'Mac 10.8'
            desired_capabilities.append(desired_capability)
            
        elif self.browser_type == Browser.ANDROID:
            desired_capability = desired_capability_base()
            desired_capability['version']    = '4'
            desired_capability['platform']   = 'Linux'
            desired_capabilities.append(desired_capability)
        
        return desired_capabilities
            
    def start_user(self, desired_capability, url):
        print "des_cap ready to get in"
        self.driver = webdriver.Remote(
                                       desired_capabilities=desired_capability, 
                                       command_executor="http://bschael:63bd1368-87eb-41a6-a2a8-d668b71a5997@ondemand.saucelabs.com:80/wd/hub"
                                       )
        self.driver.get(url)
        self.verificationErrors = []
        
    def finish_user(self):
        self.driver.quit()
            
def users_elements():
    # This is when the invitation is sent

    if 'android' in sys.argv:
        
        version              ='null'
        test_name            = sys.argv[2]
        print test_name
        
        email_user_one       = "calor.sidhuson@gmail.com"
        username_one         = "calor.sidhuson"
        id_user_one          = "100004652912112"
        name_user_one        = "Carol"
        full_name_user_one   = FBUsers.ie_name_user1
        
        email_user_two       = "dick.zuckerescu@gmail.com"
        username_two         = "dick.zuckerescu"
        id_user_two          = "100004665662931"
        name_user_two        = "Dick"
        full_name_user_two   = FBUsers.ie_name_user2
        
        email_user_three     = "rick.occhinoberg@gmail.com"
        username_three       = "rick.occhinoberg"
        id_user_three        = "100004654982066"
        name_user_three      = "Rick"
        full_name_user_three = FBUsers.ie_name_user3
        
        password             = FBLogin.fb_password
        email_link           = "http://w.test.oona.ir/#iFbmsIytz"
        browser_type          = Browser.ANDROID
        
        user = TestUser(version, test_name, email_user_one, username_one, id_user_one, name_user_one, full_name_user_one, email_user_two, username_two, id_user_two, name_user_two, full_name_user_two, email_user_three, username_three, id_user_three, name_user_three, full_name_user_three, password, email_link, browser_type)
   
    elif 'iphone' in sys.argv:
        
        version              ='null'
        test_name            = sys.argv[2]
        print test_name
        
        email_user_one       = "dick.greenestein@gmail.com"
        username_one         = "dick.greenestein"
        id_user_one          = "100004644842040"
        name_user_one        = "Dick"
        full_name_user_one   = FBUsers.ff_name_user1
        
        email_user_two       = "helen.sharpesky@gmail.com"
        username_two         = "helen.sharpesky"
        id_user_two          = "100004677001579"
        name_user_two        = "Helen"
        full_name_user_two   = FBUsers.ff_name_user2
        
        email_user_three     = "mark.carrierosky@gmail.com"
        username_three       = "mark.carrierosky"
        id_user_three        = "100004643882072"
        name_user_three      = "Mark"
        full_name_user_three = FBUsers.ff_name_user3
        
        password             = FBLogin.fb_password
        email_link           = "http://w.test.oona.ir/#iLSqQNrHL"
        browser_type         = Browser.IPHONE
        
        user = TestUser(version, test_name, email_user_one, username_one, id_user_one, name_user_one, full_name_user_one, email_user_two, username_two, id_user_two, name_user_two, full_name_user_two, email_user_three, username_three, id_user_three, name_user_three, full_name_user_three, password, email_link, browser_type)
    
    elif 'ipad' in sys.argv:
        
        version              ='null'
        test_name            = sys.argv[2]
        print test_name
        
        email_user_one       = "tom.fergiesky@gmail.com"
        username_one         = "tom.fergiesky"
        id_user_one          = "100004662542875"
        name_user_one        = "Tom"
        full_name_user_one   = FBUsers.gc_name_user1
        
        email_user_two       = "dave.qinstein@gmail.com"
        username_two         = "dave.qinstein"
        id_user_two          = "100004692991526"
        name_user_two        = "Dave"
        full_name_user_two   = FBUsers.gc_name_user2
        
        email_user_three     = "harry.letuchysen@gmail.com"
        username_three       = "harry.letuchysen"
        id_user_three        = "100004672412849"
        name_user_three      = "Harry"
        full_name_user_three = FBUsers.gc_name_user3
        
        password             = FBLogin.fb_password
        email_link           = "http://w.test.oona.ir/#iaN9fGPpb"
        browser_type         = Browser.IPAD

        user = TestUser(version, test_name, email_user_one, username_one, id_user_one, name_user_one, full_name_user_one, email_user_two, username_two, id_user_two, name_user_two, full_name_user_two, email_user_three, username_three, id_user_three, name_user_three, full_name_user_three, password, email_link, browser_type)
        
    return user

user= users_elements()