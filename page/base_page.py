# -*- Coding: utf-8 -*-
# Author: Yu
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging
import os


def dir_path(filename, filepath="data"):
    dir_path_data = os.path.join((os.path.dirname(os.path.dirname(__file__))), filepath, filename)
    return dir_path_data


# 将异常处理写成装饰器
def exception_handle(func):
    def wrapper(*args, **kwargs):
        # 引用下面得Base_page对象
        _self: Base_page = args[0]
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            if _self._error_count > _self._error_max:
                raise e
            _self._error_count += 1
            for element in _self._black_list:
                elements = _self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                return wrapper(*args, **kwargs)
            raise e
    return wrapper


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
    @exception_handle
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, value)

    def text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def find_by_text(self, key):
        return self.find(self.text(key))

    # # 找到该元素，获取该按钮的文本装饰器
    # def find_and_get_text(func):
    #     def wrapper(self, *args, **kwargs):
    #         locator = func(self)
    #         element = self.find(locator)
    #         result = element.text
    #         return result
    #     return wrapper
