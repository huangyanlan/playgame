import sys

import pygame

def check_events():
    """监控鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()