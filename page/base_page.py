# -*- Coding: utf-8 -*-
# Author: Yu
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging


class Base_page(object):
    logging.basicConfig(level=logging.INFO)
    _driver = WebDriver
    # 处理异常弹窗，选取元素黑名单
    _black_list = [
        (By.ID, "tv_agree"),
        (By.XPATH, '//*[@text="确定"]'),
        (By.ID, "image_cancel"),
        (By.XPATH, '//*[@text="下次再说"]')
    ]
    _error_max = 5
    _error_count = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # 重写find_element方法
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        try:
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            # if isinstance(locator, tuple):
            #     element = self._driver.find_element(*locator)
            # else:
            #     self._driver.find_element(locator, value)
            return element
        except Exception as e:
            if self._error_count > self._error_max:
                raise e
            self._error_count += 1
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(locator, value)
            raise e
