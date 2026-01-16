from pygame import *

class GameSprite(sprite.Sprite):
   #class constructor
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (55, 55))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


class Enemy(GameSprite):
   def update(self):
       if self.rect.x <= 470:
           self.side = "right"
       if self.rect.x >= win_width - 85:
           self.side = "left"
       if self.side == "left":
           self.rect.x -= self.speed
       else:
           self.rect.x += self.speed

class Wall(sprite.Sprite):
   def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       super().__init__()
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
       self.image = Surface((self.width, self.height))
       self.image.fill((color_1, color_2, color_3))
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
   def draw_wall(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
       #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("PythonStart2-MazeGame/background.jpg"), (win_width, win_height))


player = Player('PythonStart2-MazeGame/hero.png', 5, win_height - 80, 4)
monster = Enemy('PythonStart2-MazeGame/cyborg.png', win_width - 80, 280, 2)
final = GameSprite('PythonStart2-MazeGame/treasure.png', win_width - 120, win_height - 80, 0)


w1 = Wall(255, 0, 0, 100, 20, 450, 10) #atas
w2 = Wall(255, 0, 0, 100, 480, 350, 10) #bawah
w3 = Wall(255, 0, 0, 100, 20 , 10, 380) #kiri
w4 = Wall(255, 0, 0, 550, 20, 10, 380) #kanan
w5 = Wall(255, 0, 0, 100, 200, 450, 10) #tengah
w6 = Wall(255, 0, 0, 100, 400, 460, 10) #tengah


game = True
finish = False
clock = time.Clock()
FPS = 60


font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

mixer.init()
mixer.music.load('PythonStart2-MazeGame/pacman.mpeg')
mixer.music.play()

money = mixer.Sound('PythonStart2-MazeGame/mario-win.mp3')
kick = mixer.Sound('PythonStart2-MazeGame/mario-lose.mp3')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()
        
        player.reset()
        monster.reset()
        final.reset()


        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()


    #“Losing” situation
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2)or sprite.collide_rect(player, w3):
        finish = True
        window.blit(lose, (200, 200))
        mixer.music.stop()
        kick.play()


    #“Winning” situation
    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        mixer.music.stop()
        money.play()


    display.update()
    clock.tick(FPS)