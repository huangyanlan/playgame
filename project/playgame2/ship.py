import pygame


class Ship():

    def __init__(self,screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.sect = self.image.get_rect()
        self.screen_sect = screen.get_rect()
        # 将每艘新飞船放在屏幕中央
        self.sect.centerx= self.screen_sect.centerx
        self.sect.centery = self.screen_sect.centery

    def blitme(self):

        self.screen.blit(self.image,self.sect)