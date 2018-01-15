import json
import os
from splinter import Browser

class Chrome:
    def __init__(self):
        envConfig = json.loads(open('config\\browser.json').read())
        executable_path = {'executable_path': envConfig["browser"]["chromedriver"]}
        self.browser = Browser('chrome', **executable_path)

    def Open(self, Url):
        self.browser.visit(Url)

    def Fill(self, xpath, value):
    	self.browser.find_by_xpath(xpath).fill(value)

    def Click(self, xpath):
    	self.browser.find_by_xpath(xpath).click()
