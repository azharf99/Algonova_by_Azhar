#Create your own shooter
from random import randint
from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Shooter')

# Set window background
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
window.blit(background, (0, 0))


# Aktifkan font di game
font.init()
font = font.Font(None, 36)


# Nyalakan musik
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

missed_enemies = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, image_width=65, image_height=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (image_width, image_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, image_width=5, image_height=15):
        super().__init__(player_image, player_x, player_y, player_speed, image_width, image_height)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


bullets = sprite.Group()
enemies = sprite.Group()

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.score = 0
        super().__init__(player_image, player_x, player_y, player_speed)
    
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            self.fire()

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 10)
        bullets.add(bullet)

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(40, 660)
            global missed_enemies
            missed_enemies += 1


player = Player('rocket.png', 320, 430, 10)

for i in range(5):
    enemy = Enemy('ufo.png', randint(40, 660), 0, randint(2, 5))
    enemies.add(enemy)

finish = False
run = True
while run:
    #"Close" button press event
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        #update the background
        window.blit(background,(0,0))

        # Render the score
        score_text = font.render(f'Score: {player.score}', True, (255, 255, 255))
        window.blit(score_text, (10, 10))

        # Musuh yang terlewat
        missed_enemies_text = font.render(f'Missed Enemies: {missed_enemies}', True, (255, 255, 255))
        window.blit(missed_enemies_text, (10, 50))

        #launch sprite movements
        player.update()
        bullets.update()

        #update them in a new location in each loop iteration
        player.reset()
        enemies.draw(window)
        enemies.update()
        bullets.draw(window)

        display.update()
    #the loop is executed each 0.05 sec
    time.delay(50)