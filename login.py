# -*- coding: utf-8 -*-
# This script covers some of the login actions that repeat itself through the tests
#
# Created by Bárbara Schael Hernández
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from elements import *
import time


def FB_Login(driver, user, passwd):
    
    handle = []
    handle = driver.window_handles
    driver.switch_to_window(handle[1])

    driver.find_element_by_id(FBLogin.fb_email).clear()
    driver.find_element_by_id(FBLogin.fb_email).send_keys(user)
    driver.find_element_by_id(FBLogin.fb_passwd).clear()
    driver.find_element_by_id(FBLogin.fb_passwd).send_keys(passwd)
    driver.find_element_by_id(FBLogin.fb_login).click()
    
    driver.switch_to_window(handle[0])
    driver.switch_to_default_content()
    
    WebDriverWait(driver, 20).until(lambda driver : driver.find_element_by_css_selector(EShop.drop_overlay))
    driver.find_element_by_css_selector(EShop.drop_overlay).click()

def is_element_present(how, what):
    try: driver.find_element(by=how, value=what)
    except NoSuchElementException, e: return False
    return True
        
