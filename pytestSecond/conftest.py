#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
------------------------------------
@Time : 2020/11/23
@Auth : guqiongxin
------------------------------------
"""

'''
作业1：
1、补全计算器（加减乘除）的测试用例
2、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
3、将 Fixture 方法存放在conftest.py ，设置scope=module
'''

import os
import pytest
import yaml


@pytest.fixture(scope='function', autouse=True)
def updown():
    print('开始计算')
    yield
    print('计算结束')


@pytest.fixture(scope='module')
def tobeornottobe():
    print('测试用例开始执行')
    yield
    print('测试工作结束')


def getData(k1, k2):
    dataPath = os.path.dirname(__file__)
    with open(dataPath + '/data.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        value = data[k1][k2]
        return value
    # data = yaml.safe_load(open("./mqttData.yml", encoding='utf-8'))
