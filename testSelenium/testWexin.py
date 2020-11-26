#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 下午10:14
# @Author : guqiongxin
# @File : testWexin.py
# @Software: PyCharm
import shelve
from time import sleep
import json
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWexin():
    def setup_method(self, method):
        # 声明一个变量，设置为chrometoptions
        chrome_opts = webdriver.ChromeOptions()
        # set address same as chrome debugging port
        chrome_opts.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_weixin_sleep(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        sleep(30)
        cookies = self.driver.get_cookies()
        with open("cookies.txt", "w") as f:
            json.dump(cookies, f)

    def test_cookie(self):
        # 先打开企业微信的页面，才能传cookies进去
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("cookies.txt", "r") as f:
            # 从文件获取cookies，并转化成list对象
            cookies: List[Dict] = json.load(f)

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        sleep(2)
        self.driver.find_element(By.ID, "menu_contacts").click()

    def testCookies(self):
        # shelve 小型数据库,对象持久化保存
        db = shelve.open("logincookies")
        # db['cookie'] = cookies
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        sleep(2)
        self.driver.find_element(By.ID, "menu_contacts").click()

    def testImportConnact(self):
        db = shelve.open("logincookies")
        # db['cookie'] = cookies
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            '/Users/guqiongxin/Downloads/tongxunlu.xlsx')
        assert 'tongxunlu.xlsx' == self.driver.find_element(By.CSS_SELECTOR,
                                                            '.ww_fileImporter_fileContainer_fileNames').text
