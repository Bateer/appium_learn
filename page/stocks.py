# -*- Coding: utf-8 -*-
# Author: Yu
from appium.webdriver.common.mobileby import MobileBy
import yaml
from page.base_page import Base_page
from page.base_page import dir_path


class Stocks(Base_page):
    # subscribe
    def one_add_selected(self):
        element = self.find(MobileBy.ID, "subscribe")
        element.click()
        return self

    def stocks_text_write_yaml(self):
        stocks_list = []
        element_list = self._driver.find_elements(MobileBy.ID, "portfolio_stockName")
        for i in range(len(element_list)):
            element = element_list[i]
            stocks_list.append(element.text)
        with open(dir_path(filename="stocks.yaml"), "w", encoding="utf-8") as f:
            yaml.dump(stocks_list, f)

    def selected_stocks_text(self):
        stocks_list = []
        element_list = self._driver.find_elements(MobileBy.ID, "portfolio_stockName")
        for i in range(len(element_list)):
            element = element_list[i]
            stocks_list.append(element.text)
        with open(dir_path(filename="stocks.yaml"), "w", encoding="utf-8") as f:
            yaml.dump(stocks_list, f)
