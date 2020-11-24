#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
------------------------------------
@Time : 2020/11/23
@Auth : guqiongxin
------------------------------------
"""

'''
加减乘除四个计算方法
'''


class Calculator:
    def add(self, a, b):
        try:
            result = a + b
        except TypeError as e:
            print('输入的数值类型错误', e)
            raise TypeError
        else:
            return result

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError()
        try:
            result = a / b
        except TypeError as e:
            print('输入的数值类型错误', e)
            raise TypeError
        else:
            return round(result, 2)