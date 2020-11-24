#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
------------------------------------
@Time : 2020/11/23
@Auth : guqiongxin
------------------------------------
"""
import pytest
import allure

from pytestSecond.calculator.calculator import Calculator
from pytestSecond.conftest import getData

"""
作业2：
1、编写用例顺序：加- 除-减-乘
2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
3、本地生成测试报告
本次测试使用pytest-ordering插件控制用例的执行顺序
    @pytest.mark.run(order=ordernum)
    每个测试方法分别使用不同类型的有效与无效等价划分取值，控制用例执行顺序为加减乘除
"""


class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()

    def teardown_class(self):
        pass

    # 测试整形数相加
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(['a', 'b', 'expected'], getData("add", "intDatas"))
    def test_addInt(self, a, b, expected):
        result = self.cal.add(a, b)
        assert result == expected, f'实际结果{result}与预期结果{expected}不一致'

    # 测试浮点型数相加
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(['a', 'b', 'expected'], getData("add", "floatDatas"))
    def test_addFloat(self, a, b, expected):
        result = self.cal.add(a, b)
        assert result == expected, f'实际结果{result}与预期结果{expected}不一致'

    # 测试加法异常
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(['a', 'b'], getData("add", "raiseValue"))
    def test_addRaise(self, a, b):
        with pytest.raises(TypeError):
            self.cal.add(a, b)

    # 测试整形除法
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize(['a', 'b', 'expected'], getData("div", "intDatas"))
    def test_divInt(self, a, b, expected):
        result = self.cal.div(a, b)
        assert result == expected, f'实际结果{result}与预期结果{expected}不一致'

    # 测试浮点型数除法
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize(['a', 'b', 'expected'], getData("div", "floatDatas"))
    def test_divFloat(self, a, b, expected):
        result = self.cal.div(a, b)
        assert result == expected, f'实际结果{result}与预期结果{expected}不一致'

    # 测试除法异常
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize(['a', 'b'], getData("div", "raiseValue"))
    def test_divRaise(self, a, b):
        with pytest.raises((ZeroDivisionError, TypeError)):
            self.cal.div(a, b)

    # 测试整形乘法
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize(['a', 'b', 'expected'], getData("mul", "intDatas"))
    def test_mulInt(self, a, b, expected):
        result = self.cal.mul(a, b)
        assert result == expected, f'实际结果{result}与预期结果{expected}不一致'

    # 测试浮点型数乘法
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize(['a', 'b', 'expected'], getData("mul", "floatDatas"))
    def test_mulFloat(self, a, b, expected):
        result = self.cal.mul(a, b)
        assert result == expected, f'实际结果{result}与预期结果{expected}不一致'

    # 测试乘法异常
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize(['a', 'b'], getData("mul", "raiseValue"))
    def test_mulRaise(self, a, b):
        with pytest.raises(TypeError):
            self.cal.mul(a, b)

    # 测试整形减法
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(['a', 'b', 'expected'], getData("sub", "intDatas"))
    def test_subInt(self, a, b, expected):
        result = self.cal.sub(a, b)
        assert result == expected, f'实际结果{result}与预期结果{expected}不一致'

    # 测试浮点型数减法
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(['a', 'b', 'expected'], getData("sub", "floatDatas"))
    def test_subFloat(self, a, b, expected):
        result = self.cal.sub(a, b)
        assert result == expected, f'实际结果{result}与预期结果{expected}不一致'

    # 测试减法异常
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(['a', 'b'], getData("sub", "raiseValue"))
    def test_subRaise(self, a, b):
        with pytest.raises(TypeError):
            self.cal.sub(a, b)


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])
