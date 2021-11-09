import sys
import pygame
from settings import settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_higth))
    pygame.display.set_caption("alien invasion")

    # 设置背景颜色
    #bg_color = (230,230,230)
    ship = Ship(screen)
    #开始游戏主循环

    while True:

        #监视键盘和鼠标事件
        #for event in pygame.event.get():
           #if event.type == pygame.QUIT:
                #sys.exit()
        gf.check_events()
        # 每次循环都重绘屏幕
        screen.fill(ai_settings.screen_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()