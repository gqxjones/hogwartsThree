#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""
from random import randint
from time import sleep


def fight():
    my_hp = 1000
    my_power = randint(20, 100)
    enemy_hp = 1000
    enemy_power = randint(20, 100)

    while True:
        # 敌人发起进攻，查看我剩余血量
        my_hp = my_hp - enemy_power
        print(f"我还剩{my_hp}血量。")

        # 我发起进攻，查看敌人剩余血量
        enemy_hp = enemy_hp - my_power
        print(f"敌人还剩{enemy_hp}血量。")

        sleep(0.1)
        # 当进攻一次后判断，我的血量小于0，跳出循环，输出敌人赢了
        if my_hp <= 0:
            print("敌人赢了")
            break
        # 当进攻一次后判断，敌人血量小于0，跳出循环，输出我赢了
        elif enemy_hp <= 0:
            print("我赢了")
            break



if __name__ == '__main__':
    fight()
