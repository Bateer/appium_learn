# -*- Coding: utf-8 -*-
# Author: Yu
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging
import os


def dir_path(filename, filepath="data"):
    dir_path_data = os.path.join((os.path.dirname(os.path.dirname(__file__))), filepath, filename)

    return dir_path_data


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
            # 利用黑名单中的元素遍历出来在页面中找，找到就点击掉，再递归重新找需要的元素
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

    def text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def find_by_text(self, key):
        return self.find(self.text(key))

    # 找到该元素，获取该按钮的文本装饰器
    def find_and_get_text(func):
        def wrapper(self, *args, **kwargs):
            locator = func(self)
            element = self.find(locator)
            result = element.text
            return result
        return wrapper

    # 添加data公用路径


