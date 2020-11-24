#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
------------------------------------
@Time : 2020/11/23
@Auth : guqiongxin
------------------------------------
"""


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def walk(self):
        print('我是人，我会走路')


class Man(Person):
    def __init__(self, name, gender, high, weight):
        super().__init__(name, gender)
        self.high = high
        self.weight = weight

    def introduce(self):
        print(f'我是{self.name}，身高{self.high}，体重{self.weight}')

    def walk(self):
        print('我是男人，我走的很快')


class Woman(Person):
    def __init__(self, name, gender, dress):
        super().__init__(name, gender)
        self.dress = dress

    def walk(self):
        print(f'我叫{self.name},我穿着{self.dress}慢慢走')


if __name__ == '__main__':
    person1 = Person('zz', '女')
    person1.walk()
    man1 = Man('zhangsan', '男', '160cm', '60kg')
    woman1 = Woman('meimei', '女', '红衬衫')
    man1.introduce()
    man1.walk()
    woman1.walk()
