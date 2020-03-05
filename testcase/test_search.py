# -*- Coding: utf-8 -*-
# Author: Yu
import pytest
from page.app import App
from page.base_page import Base_page, dir_path
import yaml


class TestSearch(object):
    def setup(self):
        self.main = App().start().main()

    # 进行数据驱动
    @pytest.mark.parametrize(("key", "stock_type", "price"),
                             yaml.safe_load(open(dir_path(filename='search.yaml'))))
    def test_search(self, key, stock_type, price):
        assert self.main.goto_search_page().search(key).get_price(stock_type) > price

    def test_select(self):
        assert "已添加" in self.main.goto_search_page().search("jd").add_select().get_message()

    def test_selected_stocks(self):
        self.main.goto_stocks().one_add_selected().stocks_text_write_yaml()
        list_stocks = yaml.safe_load(open(dir_path(filename='stocks.yaml')))
        assert "特斯拉" in list_stocks


if __name__ == "__main__":
    pytest.main()
