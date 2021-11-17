#!/usr/bin/env python
# -*- coding: utf-8 -*-
#         Time:  2021/11/7 18:46
#       Author:  曹忠伟
#         File:  plane_mian.py
#     Software:  PyCharm
#  explanation:  主模块。负责游戏的启动、初始化等。

import pygame
from plance_sprite import GameSprite

class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")
        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode((480, 700))

        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()

        # 3.调用私有方法，创建精灵和精灵组
        self.__create_sprite__()

    def __create_sprite__(self):
        pass

    def start_game(self):
        print("游戏开始")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(60)
            # 2.时间监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新、绘制精灵组
            self.__update_sprite()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():
            # 判断用户是否点击了退出按钮
            if event.type == pygame.QUIT:
               PlaneGame.__game_over()

    def __check_collide(self):
        pass

    def __update_sprite(self):
        pass

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()

if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
