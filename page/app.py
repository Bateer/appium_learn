# -*- Coding: utf-8 -*-
# Author: Yu
from appium import webdriver

from page.main_page import Main_page


class App(object):
    def start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return self
    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return Main_page()
