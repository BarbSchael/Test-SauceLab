# -*- coding: utf-8 -*-
# This script covers all the elements used on different tests
# It is important to keep it updates so the tests will work
# Each variable have an element related and the intention is to make the variables
# as simple and intuitive as possible.
#
# Created by Bárbara Schael Hernández

from elements import *

class M_URL(object):
    
    url_eshopbuild    = "http://eshopbuild.test.oonair.net"
    url_eshopdevel    = "http://eshopdevel.test.oonair.net"
    url_zaradevel     = "http://zaradevel.test.oonair.net"
    url_fb            = "http://www.facebook.com"
    url_gmail         = "http://www.gmail.com"
    
class M_GMailLogin(object):
    
    gm_email          = "Email"       # This is an ID
    gm_passwd         = "Passwd"      # This is an ID
    gm_login          = "signIn"      # This is an ID
    gm_password       = "b12358781"

class M_FBLogin(object):
    
    fb_email          = "email"          # This is an ID
    fb_passwd         = "pass"           # This is an ID
    fb_login          = "loginbutton"    # This is an ID
    fb_password       = "123456"
    
class M_FBUsers(object):
    
    # iPhone tests' users
    iPhone_user1          = "dick.greenestein@gmail.com"
    iPhone_id_user1       = "100004644842040"
    iPhone_user2          = "helen.sharpesky@gmail.com"
    iPhone_id_user2       = "100004677001579"
    iPhone_user3          = "mark.carrierosky@gmail.com"
    iPhone_id_user3       = "100004643882072"
    
    # iPad tests' users
    iPad_user1          = "tom.fergiesky@gmail.com"
    iPad_id_user1       = "100004662542875"
    iPad_user2          = "dave.qinstein@gmail.com"
    iPad_id_user2       = "100004692991526"
    iPad_user3          = "harry.letuchysen@gmail.com"
    iPad_id_user3       = "100004672412849"
    
    # Android Explorer tests' users
    Android_user1          = "calor.sidhuson@gmail.com"
    Android_id_user1       = "100004652912112"
    Android_user2          = "dick.zuckerescu@gmail.com"
    Android_id_user2       = "100004665662931"
    Android_user3          = "rick.occhinoberg@gmail.com"
    Android_id_user3       = "100004654982066"


class M_Email(object):
    # EShop Build S.L.
    eshopbuild_new_email        = "//div[@class='Ki Qn']/b[contains(text(),'eshopbuild s.l.')]"     #
    eshopbuild_email            = "//div[@class='Ki Qn'][contains(text(),'eshopbuild s.l.')]"
    show_more_text_es           = "//*[contains(text(),'- Mostrar texto citado -')]"
    show_more_text_en           = "//*[contains(text(),'- Mostrar texto citado -')]"
    iPhone_user_image           = "img[src='https://graph.facebook.com/"+M_FBUsers.iPhone_id_user1+"/picture']"
    iPad_user_image             = "img[src='https://graph.facebook.com/"+M_FBUsers.iPad_id_user1+"/picture']"
    Android_user_image          = "img[src='https://graph.facebook.com/"+M_FBUsers.Android_id_user1+"/picture']"
    button_joinnow              = "a[title='join now']"
    button_goshopping           = "a[title='GO SHOPPING']"
    button_replymessage         = "a[title='Reply']"
    mobile_web                  = "div.uq a"
    link_iphone                 = "http://w.test.oona.ir/#iLSqQNrHL"
    link_ipad                   = 'http://w.test.oona.ir/#iaN9fGPpb'
    link_android                = 'http://w.test.oona.ir/#iFbmsIytz'
    
    
    # EShop Test S.L.
    eshoptest_new_email        = "//div[@class='lj Nn ']/div[@class='Rn']"
    

class M_FBMsg(object):
    fb_email                    = "div.input.inputWrapper input[name='email']"
    fb_pass                     = "div.input.inputWrapper input[name='pass']"
    fb_login                    = "button[name='login']"
    cancel_button               = "a[text='Cancel']"
    fb_msgs                     = "//div[@id='messages_jewel']/div/a" #"div#m-future-header div#messages_jewel i" 
    fb_see_more                 = "div.title.mfsm.fcl span"
    fb_friend_msg               = "div#threadlist_rows div.title.mfsl.fcb"
    fb_msg_text                 = "//div[@data-sigil='message-text']/span/a[1]"
    
    
class M_Warning(object):
    # No App Available
    black_button                = "div.main-content div div.redirection-button.black"
    msg_mobile_dev              = 'Shop with Friends is not available on mobile devices yet!'
    warning_text                = "div.redirection-intro div.redirection-intro-text"
    
    # Invite Chat Mobile
    invite_chat_mobile          = "http://w.test.oona.ir/#iM8VpXyIN"
    title_msg                   = "div.header div.main-title"
    company_name                = "eshoptests s.l."
    fb_button                   = "facebookLogin"
    msg_chat_mobile             = "You're a click away to start chatting privately with Dick."
    welcome_description         = "div.welcome-subpanel p.welcome-description"
    friend_img                  = 'div.friend-image img[src="https://graph.facebook.com/'
    iphone_friend_img           = 'div.friend-image img[src="https://graph.facebook.com/'+M_FBUsers.iPhone_id_user1+'/picture"]'
    android_friend_img          = 'div.friend-image img[src="https://graph.facebook.com/'+M_FBUsers.Android_id_user1+'/picture"]'
    product_img_4               = 'div.product img[src="http://eshoptestsl.test.oonair.net/public/imgs/prods/blazers/4a.jpg"]'
    product_img_3               = 'div.product img[src="http://eshoptestsl.test.oonair.net/public/imgs/prods/blazers/3a.jpg"]'
    friend_action               = "div.friend-action p"
    
    #Message Chat Mobile
    fb_new_msg                  = "http://w.test.oona.ir/#irO9LZU15"
    fb_new_product              = "http://w.test.oona.ir/#ib6OF2Mrd"
    fb_like_product             = "http://w.test.oona.ir/#irO9LZU15"
    element_new_comment         = "div.friend-quote-layer div p"
    new_comment                 = '''"Hey, Are you comming?"'''
    
    # Product Love
    product_love                = 'Dick loves this product'
    product_message             = 'Dick sent you a new message'
    product_share               = "Hey! I'm not sure on buying this product. Could you help me now?"
    product                     = "Zipped Blazer with Frill at the Waist"
    welcome_product             = "div.welcome-subpanel p"
    
    
    # App Available
    container_invite            = "div.redirection-invite-container"
    main_title_app              = "div.redirection-main-title"
    pic_friend_app              = 'div.redirection-image img[src="https://graph.facebook.com/100004644842040/picture"]'
    button_open_app             = "//div[@class='redirection-button black'][contains(text(),'Open in App')]"
    button_get_app              = "//div[@class='redirection-button black'][contains(text(),'Get the App')]"
    
class M_Chat(object):
    
    send_chat_msg               = "send_button"
    write_chat_msg              = "enter_chat"
    bubble_msg                  = "div#messages_stream_wrapper ul li.bubble-container.right"
    product_one_stream          = "div#productHolder0 div.product-image img"
    product_one_love            = "div#products_container div#productHolder0 div.like"
    love_product                = "addLikeButton"
    product_love_stream         = "div#products_container div#productHolder0 div.like.liked.mine"
    chat_love_stream            = "div#messages_stream_wrapper ul li.conversation-row.product div.product-data.like-data"
    love_product_msg            ="You love Zipped Blazer with Frill at the Waist"
    
    
    
    
    