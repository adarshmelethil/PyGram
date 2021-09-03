from selenium.webdriver.common import keys
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from xpath_library import XPATHS
import selenium_utils as su
from selenium_utils import log_error

def cookie_page(driver):
    if su.search_by_xpath(driver, XPATHS["login-page"]["cookie-policy-text"]) and su.search_by_xpath(driver, XPATHS["login-page"]["cookie-policy-link"]):
        btn = su.search_by_xpath(driver, XPATHS["login-page"]["cookie-policy-accept"])    
        if btn:
            btn.click()
            return True
    log_error(driver,"cookie_page(driver), couldnt find the needed elements")
    return False

def get_instagram_app(driver):
    if su.search_by_xpath(driver, XPATHS["login-page"]["html-class-login-page"]) and su.search_by_xpath(driver, XPATHS["login-page"]["get-instagram-app"]):
        btn = su.search_by_xpath(driver, XPATHS["login-page"]["login-button"])
        if btn:
            btn.click()
            return True
    log_error(driver,"get_instagram_app(driver), couldnt find the needed elements")
    return False

def save_info(driver):
    if su.search_by_xpath(driver, XPATHS["login-page"]["save-login"]):
        btn = su.search_by_xpath(driver, XPATHS["login-page"]["not-now"])
        if btn:
            btn.click()
            return True
    log_error(driver,"save_info(driver), couldnt find the needed elements")
    return False

def login(driver, username, password):
    if su.go_to_url(driver,"https://www.instagram.com"): sleep(2)
    if cookie_page(driver): sleep(2)
    if get_instagram_app(driver): sleep(2)
    username_form = su.search_by_xpath(driver, XPATHS["login-page"]["username-form"])
    password_form = su.search_by_xpath(driver, XPATHS["login-page"]["password-form"])
    if username_form and password_form:
        username_form.send_keys(username)
        password_form.send_keys(password)
        password_form.send_keys(Keys.RETURN)
        sleep(5)
    if save_info(driver): sleep(2)
    