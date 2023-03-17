import pygame
from plane_sprites import *

pygame.init()

screen = pygame.display.set_mode((480, 700))

# 绘制背景图象
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)

# 创建敌机的精灵以及精灵组
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 5)
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    clock.tick(60)

    # 捕获事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("game over")

            # quit卸载所有模块并终止执行程序
            pygame.quit()
            exit()

    # 改变飞机的位置
    hero_rect.y -= 5

    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    enemy_group.update()

    # 在screen上绘制所有的精灵
    enemy_group.draw(screen)

    pygame.display.update()

pygame.quit()
