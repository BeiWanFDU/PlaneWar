import pygame

# 定义屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        """"飞机大战游戏精灵"""
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 调用父类方法
        super().__init__("./images/background.png")

        # 判断是否交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法实现
        super().update()

        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 调用父类方法
        super().__init__("./images/enemy1.png")
        # 指定敌机的初始随即速度

        # 指定敌机的初始随机位置
        pass

    def update(self):
        # 调用父类方法
        super().update()
        # 判断是否飞出屏幕
        pass

