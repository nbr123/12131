import pygame
import random

# 初始化Pygame
pygame.init()

# 设置屏幕大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Plants vs. Zombies")

# 定义颜色
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 定义游戏时钟
clock = pygame.time.Clock()

# 定义植物类
class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 定义僵尸类
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

# 定义子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > screen_width:
            self.kill()

# 创建植物组、僵尸组和子弹组
plants = pygame.sprite.Group()
zombies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 创建一个植物实例
plant = Plant(100, screen_height // 2)
plants.add(plant)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(plant.rect.x + 40, plant.rect.y + 15)
                bullets.add(bullet)

    # 更新僵尸和子弹
    zombies.update()
    bullets.update()

    # 检测子弹和僵尸的碰撞
    for bullet in bullets:
        zombie_hit_list = pygame.sprite.spritecollide(bullet, zombies, True)
        for zombie in zombie_hit_list:
            bullets.remove(bullet)
            bullet.kill()

    # 随机生成僵尸
    if random.randint(1, 100) == 1:
        zombie = Zombie(screen_width, random.randint(0, screen_height - 40))
        zombies.add(zombie)

    # 清屏
    screen.fill((0, 0, 0))

    # 绘制所有精灵
    plants.draw(screen)
    zombies.draw(screen)
    bullets.draw(screen)

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(30)

# 退出Pygame
pygame.quit()
