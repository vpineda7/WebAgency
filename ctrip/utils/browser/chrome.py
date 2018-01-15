import json
import os
import time
from splinter import Browser

class Chrome:
    def __init__(self):
        envConfig = json.loads(open('config\\browser.json').read())
        executable_path = {'executable_path': envConfig["browser"]["chromedriver"]}
        self.browser = Browser('chrome', **executable_path)

    def OpenWith(self, Url):
        self.browser.visit(Url)

    def Fill(self, xpath, value):
    	self.browser.find_by_xpath(xpath).fill(value)

    def Click(self, xpath):
    	self.browser.find_by_xpath(xpath).click()

    def Screenshot(self, name):
        self.browser.screenshot(name)

    def WaitUtilVisible(self, xpath, interval=1):
        while self.browser.find_by_xpath(xpath).visible == False:
            time.sleep(interval)        