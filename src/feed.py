from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from xpath_library import XPATHS
import selenium_utils as su
from selenium_utils import log_error, search_by_xpath, get_attribute, current_url

class Post:
    def __init__(self, data):
        self.data = data
    def comment(self,driver,text):
        try:
            driver.get(self.data["post-comments"])
            sleep(5)
            form = search_by_xpath(driver, XPATHS["comment-page"]["comment-form"])
            if not form: 
                return False
            form.send_keys(text + Keys.ENTER)
            #5 retries
            succes = False
            for i in range(0,5):
                sleep(1)
                if search_by_xpath(driver, "//span[contains(text(), '"+text+"')]"):
                    succes = True
                    break
            search_by_xpath(driver, XPATHS["comment-page"]["back-btn"]).click()
            sleep(2)
        except:
            return False
    def like(self):
        pass


def on_feed(driver):
    if "https://www.instagram.com/" in su.current_url(driver):
        return True
    return False

def get_feed(driver):
    if on_feed(driver):
        print(current_url(driver))
    current_posts = su.search_by_xpath(driver, XPATHS["feed-page"]["get-posts"], True)
    post_list = []
    for post in current_posts:
        #parse each loaded post into a dictionary
        formatted_post = {}
        formatted_post["post-link"] =  get_attribute(search_by_xpath(post, XPATHS["feed-page"]["post-link"]) , "href")
        formatted_post["post-owner"] = get_attribute(search_by_xpath(post, XPATHS["feed-page"]["post-owner"]), "href")
        formatted_post["post-owner"] = get_attribute(search_by_xpath(post, XPATHS["feed-page"]["post-owner"]), "href")
        formatted_post["post-comments"] = formatted_post["post-link"]+"comments"
        formatted_post["post-liked"] = formatted_post["post-link"]+"liked_by"
        formatted_post["images"] = []
        #post can contain multiple images
        all_images = search_by_xpath(post, XPATHS["feed-page"]["post-images"], True)
        for image in all_images:
            formatted_post["images"].append({
                "image-link" : get_attribute(image, "src"),
                "image-info" : get_attribute(image, "alt")
            }) 
        post_list.append(formatted_post)
    post_list = list(map(lambda x: Post(x),post_list))
    return post_list 