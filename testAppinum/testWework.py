#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
# @Time : 2020/12/13 下午3:31
# @Author : guqiongxin
# @File : testWework.py
# @Software: PyCharm
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWework:
    def setup(self):
        caps = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_addcontact(self):
        gender = '女'
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(
            'ricebug')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fow').send_keys('13900000000')
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/i6k').click()
        # time.sleep(2)
        print(self.driver.page_source)
        assert '添加成功' == self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text

    def test_deletecontact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        flag = True
        while flag:
            self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/i6i").click()
            element_list = self.driver.find_elements(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gg2']")
            print(len(element_list))
            if len(element_list) == 1:
                flag = False
            else:
                element_list[-1].click()
                self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                         'new UiScrollable('
                                         'new UiSelector().scrollable(true).instance(0))'
                                         '.scrollIntoView(new UiSelector().text("删除成员").instance(0));').click()
                self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
                self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/i6d").click()
                # sleep(2)
                # assert text not in self.driver.page_source