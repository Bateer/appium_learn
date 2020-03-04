# -*- Coding: utf-8 -*-
# Author: Yu
from appium.webdriver import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from page.base_page import Base_page
from page.search import Search
from page.stocks import Stocks


class Main_page(Base_page):

    def goto_search_page(self):
        self.find(MobileBy.ID, "tv_search").click()
        return Search(self._driver)

    # 进入行情模块中测试
    def goto_stocks(self):
        self.find(MobileBy.XPATH, '//*[@text="行情"]').click()
        return Stocks(self._driver)

    def goto_trade(self):
        pass

    def goto_profile(self):
        pass

    def goto_message(self):
        pass
