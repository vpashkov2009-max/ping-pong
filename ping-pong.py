from pygame import *
mixer.init()
font.init()
from random import randint

#окно
win = display.set_mode((700, 500))
game = True
#таймер
clock = time.Clock()
#фон
background = transform.scale(image.load('background.jpg'), (700, 500))
#фпс
fps = 60
#пременные для выигрыша и проигрфша
to_lose = False
to_win = False
lose = font.Font(None, 40)
wint = font.Font(None, 40)
text_lose1 = lose.render('PLAYER 1 LOSE!!', True, (255, 0, 0))
text_lose2 = lose.render('PLAYER 2 LOSE!!', True, (255, 0, 0))
text_win1 = wint.render('PLAYER 1 WIN!!!', True, (0, 255, 0))
text_win2 = wint.render('PLAYER 2 WIN!!!', True, (0, 255, 0))
#gamesptite 
class GameSprite(sprite.Sprite):
    def __init__(self, image1, x_hero, y_hero, speed_hero, size_1, size_2):
        super().__init__()
        self.image = transform.scale(image.load(image1), (size_1, size_2))
        self.speed_hero = speed_hero
        self.rect = self.image.get_rect()
        self.rect.x = x_hero
        self.rect.y = y_hero
        self.size1 = size_1
        self.size2 = size_2
    def blit(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
#класс для передвижения спрайта player
class Player(GameSprite):
    def __init__(self, image1, x_hero, y_hero, speed_hero, size_1, size_2):
        super().__init__(image1, x_hero, y_hero, speed_hero, size_1, size_2)
    def update(self):
        down = key.get_pressed()
        if down[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_hero
        if down[K_s] and self.rect.y < 330:
            self.rect.y += self.speed_hero
    def update_2(self):
        down = key.get_pressed()
        if down[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_hero
        if down[K_DOWN] and self.rect.y < 330:
            self.rect.y += self.speed_hero
#класс enemy
class Enemy(GameSprite):
    def __init__(self, image1, x_hero, y_hero, size_1, size_2, speed_x, speed_y):
        super().__init__(image1, x_hero, y_hero, speed_x, size_1, size_2)
        self.speed_y = speed_y
        self.speed_x = speed_x
    def update(self):
        if to_lose != True and to_win != True:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        if self.rect.y > 470 or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(racket_1, self) or sprite.collide_rect(racket_2, self):
            self.speed_x *= -1
    def to_lose_racket(self):
        if self.rect.x < 0:
            to_lose = True
            win.blit(text_lose1, (200, 200))
            win.blit(text_win2, (200, 300))
        if self.rect.x > 700:
            to_lose = True
            win.blit(text_lose2, (200, 200))
            win.blit(text_win1, (200, 300))


#ракеткf
racket_1 = Player('racket.jpeg', 20, 20, 5, 10, 170)
racket_2 = Player('racket.jpeg', 660, 20, 5, 10, 170)
#мячик
ball = Enemy('ball.png', 200, 250, 40, 40, 3, 3)
#игровой цикл
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    win.blit(background, (0,0))
    racket_1.blit()
    racket_2.blit()
    racket_1.update()
    racket_2.update_2()
    ball.blit()
    ball.update()
    ball.to_lose_racket()
    clock.tick(fps)
    display.update()        