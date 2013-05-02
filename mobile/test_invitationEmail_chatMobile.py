from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, sys, os

from utilities.elements_mobile import *
from utilities import utils
from utilities.objSetup_mobile1 import *
from string import uppercase

class InviteChatMobile(unittest.TestCase):
    
    def chat_mobile_message(self, user):
        user.driver.get(M_Warning.fb_new_msg)
        handle = []
        handle = user.driver.window_handles
        print handle

        user.driver.switch_to_window(handle[0])
        user.driver.switch_to_default_content()
        
        # Wait & Assert FB Button
        utils.wait_and_check_element(self, user.driver, M_Warning.fb_button)
        
        # Assert Title
        title=user.driver.find_element_by_css_selector(M_Warning.title_msg)
        title=title.text
        self.assertEqual(M_Warning.company_name.upper(), title.upper())
        
        # Assert Welcome Description
        compare=user.driver.find_element_by_css_selector(M_Warning.welcome_description)
        compare=compare.text
        self.assertEqual(M_Warning.msg_chat_mobile.upper(), compare.upper())
        
        # Assert User Img
        self.assertTrue(user.driver.find_element_by_css_selector(M_Warning.friend_img+user.id_user_one+'/picture"]'))
        
        # Assert Message
        comment = user.driver.find_element_by_css_selector(M_Warning.element_new_comment)
        comment= comment.text
        self.assertEqual(M_Warning.new_comment.upper(), comment.upper())
        
        # Assert user action
        action= user.driver.find_element_by_css_selector(M_Warning.friend_action)
        action= action.text
        self.assertEqual(M_Warning.product_message.upper(), action.upper())
        user.driver.get(M_URL.url_fb)
        
    def chat_mobile_love_product(self, user):
        user.driver.get(M_Warning.fb_like_product)
        handle = []
        handle = user.driver.window_handles

        user.driver.switch_to_window(handle[0])
        user.driver.switch_to_default_content()
        utils.wait_and_check_element(self, user.driver, M_Warning.fb_button)
        
        # Assert Title
        title=user.driver.find_element_by_css_selector(M_Warning.title_msg)
        title=title.text
        print title
        self.assertEqual(M_Warning.company_name.upper(), title.upper())
        
        # Assert Welcome Description
        compare=user.driver.find_element_by_css_selector(M_Warning.welcome_description)
        compare=compare.text
        self.assertEqual(M_Warning.msg_chat_mobile.upper(), compare.upper())
        
        # Assert User Img
        self.assertTrue(user.driver.find_element_by_css_selector(M_Warning.friend_img+user.id_user_one+'/picture"]'))
        
        # Assert Product Img
        self.assertTrue(user.driver.find_element_by_css_selector(M_Warning.product_img_3))
        
        # Assert user action
        love= user.driver.find_element_by_css_selector(M_Warning.friend_action)
        love= love.text
        self.assertEqual(M_Warning.product_love.upper(), love.upper())
        
    def chat_mobile_share_product(self, user):
        user.driver.get(M_URL.url_fb)
        user.driver.get(M_Warning.fb_new_product)
        handle = []
        handle = user.driver.window_handles

        user.driver.switch_to_window(handle[0])
        user.driver.switch_to_default_content()
        utils.wait_and_check_element(self, user.driver, M_Warning.fb_button)
        
        # Assert Title
        title=user.driver.find_element_by_css_selector(M_Warning.title_msg)
        title=title.text
        print title
        self.assertEqual(M_Warning.company_name.upper(), title.upper())
        
        # Assert Welcome Description
        compare=user.driver.find_element_by_css_selector(M_Warning.welcome_description)
        compare=compare.text
        self.assertEqual(M_Warning.msg_chat_mobile.upper(), compare.upper())
        
        # Assert User Img
        self.assertTrue(user.driver.find_element_by_css_selector(M_Warning.friend_img+user.id_user_one+'/picture"]'))
        
        # Assert Product Img
        self.assertTrue(user.driver.find_element_by_css_selector(M_Warning.product_img_3))
        
        # Assert user action
        share= user.driver.find_element_by_css_selector(M_Warning.friend_action)
        share= share.text
        self.assertEqual(M_Warning.product_share.upper(), share.upper())
        
        # Assert Product Title
        prod_title = user.driver.find_element_by_css_selector(M_Warning.welcome_product)
        prod_title = prod_title.text
        self.assertEqual(M_Warning.product.upper(), prod_title.upper())

    def test_mobile(self):
        print "before desired"
        for desired_capabality in user.desired_capabilities:
            user.start_user(desired_capabality, M_URL.url_gmail)
            self.chat_mobile_message(user=user)
            self.chat_mobile_love_product(user=user)
            self.chat_mobile_share_product(user=user)
            user.finish_user()
            
if __name__ == "__main__":
    if 'iphone' in sys.argv:
        sys.argv.remove('iphone')
        sys.argv.remove('Msg_ChatMobile')
         
    unittest.main() 