from pygame import *
from random import randint
# описание классов
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Platform(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__( img, x, y, w, h, speed)    
        self.x_start = x
    def update(self):
        self.rect.x =  self.rect.x+ x_pos   


class Player(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.oppora = False
    def update(self):
        global x_pos
        keys = key.get_pressed()
        if self.rect.x < x_start or self.rect.x > x_max-x_start :
            if keys[K_LEFT] and self.rect.x>10:
                self.rect.x-=self.speed
            if keys[K_RIGHT] and self.rect.x<700 -10- self.rect.width:
                self.rect.x+=self.speed
        else:
            if keys[K_LEFT] and x_pos>0:
                x_pos += self.speed

            if keys[K_RIGHT]and x_pos< x_max-x_start*2:
                x_pos -= self.speed
        
        
        if keys[K_SPACE] and self.oppora:
            self.rect.y -=70 

    def gravity(self,plt): 
        self.oppora= False 
        sprite_list = sprite.spritecollide(player,plt,False)            
        if len (sprite_list)!=0:
            self.oppora= True 

        if not self.oppora:
            self.rect.y+=1   

class Enemy(GameSprite):    
    def __init__(self, img, x, y, w, h, speed,fly=0):
        super().__init__( img, x, y, w, h, speed)     
        self.fly = fly

    def start(self,z1,z2):
        self.z1 = z1
        self.z2 = z2          
    def update(self):
        if self.fly == 1:
            if self.rect.y <= min(self.z1,self.z2):
                self.direct = 1
            elif self.rect.y >= max(self.z1,self.z2):
                self.direct = -1   
            self.rect.y += self.speed*self.direct
        else: 
            if self.rect.x <= min(self.z1,self.z2):
                self.direct = 1
            elif self.rect.y >= max(self.z1,self.z2): 
                self.direct = -1   
            self.rect.x += self.speed*self.direct    

x_start = 350-15
x_pos = 0
x_max = 1400

# создай окно игры
window = display.set_mode((700,500))
display.set_caption('Платформер')
#задай фон сцены
background = transform.scale(image.load('fon.jpg'), (700,500))

platforms =  sprite.Group()
pl_count = 10
for i in range(pl_count):
    x = randint(5,x_max-105)
    y = randint(300,450)
    plt = Platform('platf.png',x,y,100,50,0)
    platforms.add(plt)
plt = Platform('platf.png',-20,470,x_max+20,50,0)
platforms.add(plt)

player=Player('pl.png',10,300,30,40,5)
enemyes = sprite.Group()
enemy1=Enemy('enemy.png',200,200,50,60,1)
enemy1.start(200,300)
enemyes.add(enemy1)  
enemy2=Enemy('enemy.png',400,300,50,60,1,1)
enemy2.start(400,300)
enemyes.add(enemy2)  

game = True
clock = time.Clock()
fps = 60


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))
    platforms.draw(window)
    platforms.update()
    player.reset()
    player.update()
    player.gravity(platforms)
    enemyes.update()
    enemyes.draw(window)


    clock.tick(fps)
    display.update()



