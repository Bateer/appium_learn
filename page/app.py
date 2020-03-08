# -*- Coding: utf-8 -*-
# Author: Yu
import datetime
from time import sleep

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import Base_page
from page.main_page import Main_page


class App(Base_page):

    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        # 如何没有驱动创建驱动driver
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "Ranger_IDE"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["chromedriverExecutableDir"] = "D:\PyProject\chromeDriver"
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            # 如果已经有驱动了，使用start_activity方法启动
            self._driver.start_activity(self._package, self._activity)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main_page:
        # 等待主页的加载
        def wait_load(driver):
            print(datetime.datetime.now())
            source = self._driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return True
            if "image_cancel" in source:
                return True
            return False

        WebDriverWait(self._driver, 60).until(wait_load)
        return Main_page(self._driver)
