# -*- coding: utf-8 -*-
# This script covers all the elements used on different tests
# It is important to keep it updates so the tests will work
# Each variable have an element related and the intention is to make the variables
# as simple and intuitive as possible.
#
# Created by Barbara Schael Hernandez

class URL(object):
    
    url_eshopbuild    = "http://eshopbuild.test.oonair.net/"
    url_fb            = "http://www.facebook.com"
    url_gmail         = "http://www.gmail.com"
    url_google        = "http://www.google.com"

class FBLogin(object):
    
    fb_email          = "email"          # This is an ID
    fb_passwd         = "pass"           # This is an ID
    fb_login          = "loginbutton"    # This is an ID
    fb_password       = "123456"
    fb_cancel         = "//div[@id='dialog_buttons']/label[2]"
    
class FBUsers(object):
    
    # Internet Explorer tests' users
    ie_name_user1     = "Carol Amdfebiabaab Sidhuson"
    ie_user1_n          = "calor.sidhuson"
    ie_user1          = "calor.sidhuson@gmail.com"
    ie_id_user1       = "100004652912112"
    
class EShop(object):
    # EShop
    ribbon                      = "sbRibbonLabel"#"sbRibbon"
    sbopenclose                 = "a.sbopenclose"
    add_to_basket_button        = "a.button" # "//div[@class='products']/div[@class='details']/a"
    main_title_content          = "div#content h3"
    
    # Chat Pannel
    start_fb_button             = "startFBFromRightPanel"                  # This is an ID
    write_msg                   = "conversationMsgInput"                   # This is an ID
    log_out                     = "logout"                                  #"//ul[@class='settings-list']/li[1]"
    drop_overlay                = "div#dropOverlay div.close"
    hide_sb_pannel              = "hideSidebarWelcome"
    hide_sb_pannel_online       = "hideSidebar"
    
    # iframes
    eshop_iframe                = "iframeContent"
    
    # Messages
    wrong_mail                  = "Wrong Mail"
    empty_chat_msg              = "No one else is here"
    add_friend_to_chat          = "Add friend to chat"
    ssl_msg                     = "I'm in ssl test, dude..."
    
    

