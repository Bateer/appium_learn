# -*- Coding: utf-8 -*-
# Author: Yu
from appium.webdriver import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from page.search import Search


class Main_page(object):
    _driver: webdriver
    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    def goto_search_page(self):
        self._driver.find_element_by_id("tv_search").click()
        return Search()

    def goto_stocks(self):
        pass

    def goto_trade(self):
        pass

    def goto_profile(self):
        pass

    def goto_message(self):
        pass
