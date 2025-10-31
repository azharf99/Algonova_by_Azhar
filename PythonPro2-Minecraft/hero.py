key_switch_camera = 'c' # apakah kamera terhubung ke hero atau tidak
key_switch_mode = 'z' # bisa melewati rintangan atau tidak


key_forward = 'w'   # langkah maju (di mana kamera melihat)
key_back = 's'      # langkah mundur
key_left = 'a'      # langkah ke kiri (ke samping kamera)
key_right = 'd'     # langkah ke kanan
key_up = 'e'      # langkah ke atas
key_down = 'q'     # langkah ke bawah


key_turn_left = 'n'     # putar kamera ke kanan (dan dunia ke kiri)
key_turn_right = 'm'    # putar kamera ke kiri (dan dunia ke kanan)


key_build = 'b'     # bangun blok di depan Anda
key_destroy = 'v'   # hancurkan blok di depan Anda

save_map = 'k'
load_map = 'l'


class Hero():
   def __init__(self, base, pos, land, loader, render):
       self.land = land
       self.base = base
       self.loader = loader
       self.render = render
       self.mode = True # melewati semua mode
       self.hero = self.loader.loadModel('panda')
       self.hero.setColor(0.5, 0.5, 0)
       self.hero.setScale(0.3)
       self.hero.setH(180)
       self.hero.setPos(pos)
       self.hero.reparentTo(self.render)
       self.cameraBind()
       self.accept_events()


   def cameraBind(self):
       self.base.disableMouse()
       # self.base.camera.setH(180)
       self.base.camera.reparentTo(self.hero)
       self.base.camera.setPos(0, 0, 1.5)
       self.cameraOn = True


   def cameraUp(self):
       pos = self.hero.getPos()
       self.base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
       self.base.camera.reparentTo(self.render)
       self.base.enableMouse()
       self.cameraOn = False


   def changeView(self):
       if self.cameraOn:
           self.cameraUp()
       else:
           self.cameraBind()


   def turn_left(self):
       self.hero.setH((self.hero.getH() + 5) % 360)


   def turn_right(self):
       self.hero.setH((self.hero.getH() - 5) % 360)


   def look_at(self, angle):
       ''' mengembalikan koordinat ke mana karakter yang berdiri di titik (x, y) akan berpindah,
       jika dia mengambil langkah ke arah angle'''


       x_from = round(self.hero.getX())
       y_from = round(self.hero.getY())
       z_from = round(self.hero.getZ())


       dx, dy = self.check_dir(angle)
       x_to = x_from + dx
       y_to = y_from + dy
       return x_to, y_to, z_from


   def just_move(self, angle):
       '''bergerak ke koordinat yang diinginkan dalam hal apa pun'''
       pos = self.look_at(angle)
       self.hero.setPos(pos)


   def move_to(self, angle):
       if self.mode:
           self.just_move(angle)
       else:
           self.try_move(angle)
  
   def check_dir(self,angle):
       ''' mengembalikan perubahan bulat pada koordinat X, Y
       sesuai dengan gerakan menuju sudut angle.
       Koordinat Y berkurang jika karakter melihat pada sudut 0,
       dan bertambah jika dilihat dari sudut 180.   
       Koordinat X bertambah jika karakter melihat pada sudut 90,
       dan berkurang jika dilihat dari sudut 270.   
           sudut 0 (dari 0 sampai 20) -> Y - 1
           sudut 45 (dari 25 hingga 65) -> X + 1, Y - 1
           sudut 90 (dari 70 hingga 110) -> X + 1
           dari 115 hingga 155            -> X + 1, Y + 1
           dari 160 hingga 200            ->        Y + 1
           dari 205 hingga 245            -> X - 1, Y + 1
           dari 250 hingga 290            -> X - 1
           dari 290 hingga 335            -> X - 1, Y - 1
           dari  340                   ->        Y - 1  '''
       if angle >= 0 and angle <= 20:
           return (0, -1)
       elif angle <= 65:
           return (1, -1)
       elif angle <= 110:
           return (1, 0)
       elif angle <= 155:
           return (1, 1)
       elif angle <= 200:
           return (0, 1)
       elif angle <= 245:
           return (-1, 1)
       elif angle <= 290:
           return (-1, 0)
       elif angle <= 335:
           return (-1, -1)
       else:
           return (0, -1)


   def forward(self):
       angle =(self.hero.getH()) % 360
       self.move_to(angle)


   def back(self):
       angle = (self.hero.getH()+180) % 360
       self.move_to(angle)
  
   def left(self):
       angle = (self.hero.getH() + 90) % 360
       self.move_to(angle)


   def right(self):
       angle = (self.hero.getH() + 270) % 360
       self.move_to(angle)


   def changeMode(self):
       if self.mode:
           self.mode = False
       else:
           self.mode = True
  
   def try_move(self, angle):
       '''bergerak jika dia bisa'''
       pos = self.look_at(angle)
       if self.land.isEmpty(pos):
           #ada area bebas di depan kita. Mungkin Anda perlu jatuh:
           pos = self.land.findHighestEmpty(pos)
           self.hero.setPos(pos)
       else:
           # di depan kita sedang sibuk. Jika kita berhasil, mari kita panjat blok ini:
           pos = pos[0], pos[1], pos[2] + 1
           if self.land.isEmpty(pos):
               self.hero.setPos(pos)
               # kita tidak akan bisa mendaki - kita akan diam
   def up(self):
       if self.mode:
           self.hero.setZ(self.hero.getZ() + 1)


   def down(self):
       if self.mode and self.hero.getZ() > 1:
           self.hero.setZ(self.hero.getZ() - 1)
  
   def build(self):
       angle = self.hero.getH() % 360
       pos = self.look_at(angle)
       if self.mode:
           self.land.addBlock(pos)
       else:
           self.land.buildBlock(pos)


   def destroy(self):
       angle = self.hero.getH() % 360
       pos = self.look_at(angle)
       if self.mode:
           self.land.delBlock(pos)
       else:
           self.land.delBlockFrom(pos)


   def accept_events(self):
        self.base.accept(key_turn_left, self.turn_left)
        self.base.accept(key_turn_left + '-repeat', self.turn_left)
        self.base.accept(key_turn_right, self.turn_right)
        self.base.accept(key_turn_right + '-repeat', self.turn_right)

        self.base.accept(key_forward, self.forward)
        self.base.accept(key_forward + '-repeat', self.forward)
        self.base.accept(key_back, self.back)
        self.base.accept(key_back + '-repeat', self.back)
        self.base.accept(key_left, self.left)
        self.base.accept(key_left + '-repeat', self.left)
        self.base.accept(key_right, self.right)
        self.base.accept(key_right + '-repeat', self.right)


        self.base.accept(key_switch_camera, self.changeView)


        self.base.accept(key_switch_mode, self.changeMode)


        self.base.accept(key_up, self.up)
        self.base.accept(key_up + '-repeat', self.up)
        self.base.accept(key_down, self.down)
        self.base.accept(key_down + '-repeat', self.down)


        self.base.accept(key_build, self.build)
        self.base.accept(key_destroy, self.destroy)


        self.base.accept(save_map, self.land.saveMap)
        self.base.accept(load_map, self.land.loadMap)