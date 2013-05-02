# ~ Funtions created by Francesc Casellas
import logging, time
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from objSetup import *

def wait_and_check_element(unittest, browser, value, by=By.ID, timeout=60):
    """ Wait for an element and checks that the element is present into the screen
        Attributes:
            - unittest: Unitetest being used
            - browser:  Browser where the page is shown
            - by:       The locating mechanism to use
            - value:    Element Value
            -timeout:   (Optional) Time until timeout
        Results:
            If the element is not into the screen when the time is out then an error is raised
    """
    element_found = False
    for i in range(timeout):
        time.sleep(1)
        if is_element_present(browser=browser, value=value, by=by):
            element_found = True
            break
    unittest.assertTrue(element_found)
        
def is_element_present(browser, value, by=By.ID):
    """ Check if an element is currently on screen
        Attributes:
            - browser:  Browser where the page is shown
            - by:       The locating mechanism to use
            - value:    Element Value
        Returns:
            True if the element is present. Otherwise returns false
    """
    try: 
        browser.find_element(by=by, value=value)
    except Exception, e: 
        return False
    return True