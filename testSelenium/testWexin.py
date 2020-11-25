#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 下午10:14
# @Author : guqiongxin
# @File : testWexin.py
# @Software: PyCharm

from time import sleep

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

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.qq.com', 'expiry': 1606314909, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850349134979'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'Ecd8xZuaPLmmxddE1HNKVfHxlycbfAMbA7jxVOA6Rus9WM8xZeWv2dEN-7DMOwQeOmgC_rQWaJKOdCKEvPXXVlOVu7iurxLWoAhNlz35eafEwm0tjlgGC4-6wXIPXfpWSmLDBUlRqZQXUd1hTA5jZYhgbDM3clclYRizX2_b6q24niacXSHSOqJd8Tknyx8436jV5JcuFV1IvwtvBskMMsgkG_7VHDt6ceSkxVXJMnh92aZOEJqaWVES6SIGlelsQC8OyCCTCOk4PpXdQRnOPg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850349134979'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324950117443'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'TBTqlkDRb70vRP-rIUDhAqLS55K-Jy8A77aLrEIWYEkZzKb-fo3nX9fEYjGAFxPh'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1606344513, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '5iftei3'},
            {'domain': '.qq.com', 'expiry': 1606400495, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1579896707.1606312982'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '01273623'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1608906852, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1669386095, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.713897481.1606312982'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1637848977, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1608904398, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '2863798069'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a5505749'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'f00dd5e1e47089d7429d02107fe397cf4bcc459836be07f71bf380ac063ba247'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'q1jF22+HHC'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        sleep(2)
        self.driver.find_element(By.ID, "menu_contacts").click()
