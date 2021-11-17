#!/usr/bin/env python
# -*- coding: utf-8 -*-
#         Time:  2021/11/8 13:36
#       Author:  曹忠伟
#         File:  plance_sprite.py
#     Software:  PyCharm
#  explanation:  飞机精灵模块。提供所有工具

import pygame

# 定义常量
# SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在垂直方向上移动
        self.rect.y += self.speed

class Background(GameSprite):
    """游戏背景精灵"""

    def update(self):

        # 1.调用父类的方法实现
        super().update()

        # 2.图像是否移出屏幕，如果移出屏幕，将移动图像到上方
        if self.rect.y > 700:
            self.rect.y = -self.rect.height
