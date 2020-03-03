# -*- Coding: utf-8 -*-
# Author: Yu
import pytest
from page.app import App
from page.base_page import Base_page

class TestSearch(object):
    def setup(self):
        self.main = App().start().main()

    def test_search(self):
        assert self.main.goto_search_page().search("alibaba").get_price("BABA") > 200

    def test_select(self):
        assert "已添加" in self.main.goto_search_page().search("jd").add_select().get_message()


if __name__ == "__main__":
    pytest.main()
