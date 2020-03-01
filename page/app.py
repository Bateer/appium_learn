# -*- Coding: utf-8 -*-
# Author: Yu
from page.main_page import Main_page
class App(object):
    def start(self):
        return self
    def restart(self):
        pass
    def stop(self):
        pass
    def main(self):
        return Main_page()