# -*- Coding: utf-8 -*-
# Author: Yu
from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from page.base_page import Base_page


class Search(Base_page):

    def search(self, key: str):
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        self.find(MobileBy.ID, "name").click()
        return self

    def get_price(self, Key: str):
        return float(self.find(MobileBy.ID, "current_price").text)
