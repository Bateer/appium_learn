# -*- Coding: utf-8 -*-
# Author: Yu
import pytest
from page.app import App


class TestSearch(object):
    def setup(self):
        self.main = App().start().main()

    def test_search(self):
        assert self.main.goto_search_page().search("alibaba").get_price("BABA") > 200


if __name__ == "__main__":
    pytest.main()
