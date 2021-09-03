#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.common.keys import Keys
from dotenv import dotenv_values
from time import sleep
import selenium_utils as su
from login import login
import logging
import uuid 
from feed import get_feed

config = dotenv_values(".env")

class session:
    def __init__(self):
        logging.basicConfig(filename="log.log",encoding='utf-8', level=logging.DEBUG)
        FireFox_Options_Instance = Firefox_Options()
        FireFox_Options_Instance.set_preference("general.useragent.override", config["useragent"] )
        self.driver = webdriver.Firefox(executable_path="./browser_module/geckodriver",options=FireFox_Options_Instance)
        self.driver.set_window_size(375, 667)
    def __enter__(self):
        return self.driver
    def __exit__ (self, type, value, traceback):
        self.driver.close()

with session() as driver:
    login(driver, config["username"], config["password"])
    sleep(10)
    posts = get_feed(driver)
    posts[0].comment(driver, "His wife also looking hella good")
    sleep(100)
    