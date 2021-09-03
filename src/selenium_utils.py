from os import EX_PROTOCOL
from selenium import webdriver
import selenium
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.common.keys import Keys
import logging

#save every page where it errors
#this helps to progressively catch all the error cases
def log_error(driver, error_message):
    logging.error(error_message)
    driver.take_screenshot("error.png")
    logging.debug(get_attribute(driver, "InnerHTML"))
    

def current_url(driver):
    return driver.execute_script("return window.location.href")

def search_by_xpath(driver, look_for, multiple=False):
    res = ""
    try:
        if not multiple:
            res = driver.find_element_by_xpath(look_for)
        else:
            res = driver.find_elements_by_xpath(look_for)
        return res 
    except Exception as e:
        log_error(driver,"search_by_xpath" + str(e))

    if not multiple:
        try:
            res = driver.find_element_by_xpath(look_for)
        except:
            return False
    else:
        try:
            res = driver.find_elements_by_xpath(look_for)
        except:
            return False
    return res 

def get_attribute(driver, attr):
    try:
        data = driver.get_attribute(attr)
        return data 
    except:
        return False
    

def go_to_url(driver, url):
    try:
        driver.get(url)
        return True
    except Exception as e:
        return False 