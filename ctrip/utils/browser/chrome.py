import json
import os
from splinter import Browser

class Chrome:
    def __init__(self):
        with open('config\\browser.json') as envConfigFile:
            envConfig = json.load(envConfigFile)
            executable_path = {'executable_path':envConfig['browser']['chromedriver']}
            self.browser = Browser('chrome', **executable_path)

    def open(self, pageUrl):
        self.browser.visit(pageUrl)
