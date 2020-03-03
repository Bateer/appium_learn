# -*- Coding: utf-8 -*-
# Author: Yu

from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.base_page import Base_page


class Search(Base_page):

    def search(self, key: str):
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        self.find(MobileBy.ID, "name").click()
        return self

    def get_price(self, key: str):
        return float(self.find(MobileBy.ID, "current_price").text)

    def add_select(self):
        element = self.find_by_text("加自选")
        element.click()
        return self

    def un_select(self):
        element = self.find_by_text("已添加")
        element.click()
        return self

    @Base_page.find_and_get_text
    def get_message(self):
        locator = (By.ID, "followed_btn")
        return locator
