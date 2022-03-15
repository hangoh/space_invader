import random
import pygame
import os
pygame.init()
win=pygame.display.set_mode((1700,1080))
pygame.display.set_caption('SPACE INVADERS')

#enemy ship
blue_ship=pygame.image.load('/Users/gohyuhan/space_invader/pic/pixel_ship_blue_small.png')
red_ship=pygame.image.load('/Users/gohyuhan/space_invader/pic/pixel_ship_red_small.png')
green_ship=pygame.image.load('/Users/gohyuhan/space_invader/pic/pixel_ship_green_small.png')
#player ship
yellow_ship=pygame.image.load('/Users/gohyuhan/space_invader/pic/pixel_ship_yellow.png')
#enemy ship laser
blue_laser=pygame.image.load('/Users/gohyuhan/space_invader/pic/pixel_laser_blue.png')
red_laser=pygame.image.load('/Users/gohyuhan/space_invader/pic/pixel_laser_red.png')
green_laser=pygame.image.load('/Users/gohyuhan/space_invader/pic/pixel_laser_green.png')
#player ship laser
yellow_laser=pygame.image.load('/Users/gohyuhan/space_invader/pic/pixel_laser_yellow.png')
#background
bg=pygame.image.load('/Users/gohyuhan/space_invader/pic/background-black.jpg')

class Player(): 
    def __init__(self,x,y,width,height):
        self.live=5
        self.score=0
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=10
        self.stay=True
        self.up=False
        self.down=False
        self.left=False
        self.right=False
        self.shoot=False
        self.bullets=[]
        self.shootcount=0
        self.hitbox1=(self.x+30,self.y+5,self.width-60,self.height)
        self.hitbox2=(self.x+7,self.y+60,self.width-15,self.height-70)
        self.hp=10
        self.health=(self.x,self.y+self.height+3,self.hp*10,5)

    def action(self):
        if self.up:
            if self.y-self.vel>0:
                self.y-=self.vel
                self.hitbox1=(self.x+30,self.y+5,self.width-60,self.height)
                self.hitbox2=(self.x+7,self.y+60,self.width-15,self.height-70)
                self.health=(self.x,self.y+self.height+3,self.hp*10,5)
        if self.down:
            if self.y+self.vel<1080-10-self.height:
                self.y+=self.vel
                self.hitbox1=(self.x+30,self.y+5,self.width-60,self.height)
                self.hitbox2=(self.x+7,self.y+60,self.width-15,self.height-70)
                self.health=(self.x,self.y+self.height+3,self.hp*10,5)
        if self.left:
            if self.x-self.vel>0:
                self.x-=self.vel
                self.hitbox1=(self.x+30,self.y+5,self.width-60,self.height)
                self.hitbox2=(self.x+7,self.y+60,self.width-15,self.height-70)
                self.health=(self.x,self.y+self.height+3,self.hp*10,5)
        if self.right:
            if self.x+self.vel<1700-self.width:
                self.x+=self.vel
                self.hitbox1=(self.x+30,self.y+5,self.width-60,self.height)
                self.hitbox2=(self.x+7,self.y+60,self.width-15,self.height-70)
                self.health=(self.x,self.y+self.height+3,self.hp*10,5)
        if self.stay:
            self.up=False
            self.down=False
            self.left=False
            self.right=False
        if self.shoot:
            if self.shootcount==0:
                self.bullets.append(projectile(self.x,self.y))
                self.shootcount+=1
            self.shoot=False

        for bullet in self.bullets:
            bullet.y-=bullet.vel
            bullet.box=(bullet.x+45,bullet.y+27,10,30) 
        
        if self.hp==0:
            self.live-=1
            self.hp=10

    def draw(self):
        win.blit(yellow_ship,(self.x,self.y))
        #pygame.draw.rect(win,(255,0,0),self.hitbox1,2)
        #pygame.draw.rect(win,(255,0,0),self.hitbox2,2)
        pygame.draw.rect(win,(202,255,112),self.health)
        for bullet in self.bullets:
            win.blit(yellow_laser,(bullet.x,bullet.y))
            #pygame.draw.rect(win,(255,0,0),bullet.box,2)
            
#function to generate three different color of enemies at different location
def generate_enemies(enemies):
    types=['red','blue','green']
    num=random.randint(0,2)
    x=list(range(20,1611,70))
    y=list(range(5,501,50))
    x_pos=random.choice(x)
    y_pos=random.choice(y)
    if types[num]=="red":
        enemies.append(Enemy(x_pos,-y_pos,70,50,'red'))
    if types[num]=='green':
        enemies.append(Enemy(x_pos,-y_pos,70,50,'green'))
    if types[num]=="blue":
        enemies.append(Enemy(x_pos,-y_pos,50,50,'blue'))

class Enemy():
    def __init__(self,x,y,width,height,color):
        self.shootcount=250
        self.visible=True
        self.bullets=[]
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=0.5
        self.color=color
        self.score=5
        self.hitbox=(self.x+7,self.y+5,self.width-12,self.height-12)
    def action(self):
        self.y+=self.vel
        self.hitbox=(self.x+5,self.y+5,self.width-12,self.height-12)
        
    
    def draw(self):
        if self.color=="red":
            if self.shootcount==0:
                self.bullets.append(projectile(self.x-15,self.y))
                self.shootcount+=1
            for bullet in self.bullets:
                bullet.y+=bullet.vel
                bullet.box=(bullet.x+45,bullet.y+27,10,30)
            win.blit(red_ship,(self.x,self.y))
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
            for bullet in self.bullets:
                if bullet.visible:
                    win.blit(red_laser,(bullet.x,bullet.y))
                    #pygame.draw.rect(win,(255,0,0),bullet.box,2)
        
        if self.color=='green':
            if self.shootcount==0:
                self.bullets.append(projectile(self.x-15,self.y))
                self.shootcount+=1
            for bullet in self.bullets:
                bullet.y+=bullet.vel
                bullet.box=(bullet.x+45,bullet.y+27,10,30)
            win.blit(green_ship,(self.x,self.y))
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
            for bullet in self.bullets:
                if bullet.visible:
                    win.blit(green_laser,(bullet.x,bullet.y))
                    #pygame.draw.rect(win,(255,0,0),bullet.box,2)
        
        if self.color=="blue":
            if self.shootcount==0:
                self.bullets.append(projectile(self.x-25,self.y))
                self.shootcount+=1
            for bullet in self.bullets:
                bullet.y+=bullet.vel
                bullet.box=(bullet.x+45,bullet.y+27,10,30)
            win.blit(blue_ship,(self.x,self.y))
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
            for bullet in self.bullets:
                if bullet.visible:
                    win.blit(blue_laser,(bullet.x,bullet.y))
                    #pygame.draw.rect(win,(255,0,0),bullet.box,2)

#class for bullet for both player character and enemy
class projectile():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=100
        self.height=90
        self.box=(self.x+45,self.y+27,10,30)   
        self.vel=10
        self.visible=True

#function to determine if a collision between character and enemy or character with projectile or enemy with projectile has occured 
def collide(p,enemies,t1,t2,FPSTIMER):
    #collision between ships
    for enemy in enemies:
        if enemy.hitbox[0]>p.hitbox2[0] and enemy.hitbox[0]<(p.hitbox2[0]+p.hitbox2[2]) and enemy.visible:
            if (enemy.hitbox[1]+enemy.hitbox[3])>p.hitbox1[1] and (enemy.hitbox[1]+enemy.hitbox[3])<(p.hitbox1[1]+p.hitbox1[3]):
                enemy.visible=False
                p.hp-=1
                p.health=(p.x,p.y+p.height+3,p.hp*10,5)
            if (enemy.hitbox[1]+enemy.hitbox[3])>p.hitbox2[1] and (enemy.hitbox[1]+enemy.hitbox[3])<(p.hitbox2[1]+p.hitbox2[3]):
                enemy.visible=False
                p.hp-=1
                p.health=(p.x,p.y+p.height+3,p.hp*10,5)
        if (enemy.hitbox[0]+enemy.hitbox[2])>p.hitbox2[0] and (enemy.hitbox[0]+enemy.hitbox[2])<(p.hitbox2[0]+p.hitbox2[2]) and enemy.visible:
            if (enemy.hitbox[1]+enemy.hitbox[3])>p.hitbox1[1] and (enemy.hitbox[1]+enemy.hitbox[3])<(p.hitbox1[1]+p.hitbox1[3]):
                enemy.visible=False
                p.hp-=1
                p.health=(p.x,p.y+p.height+3,p.hp*10,5)
            if (enemy.hitbox[1]+enemy.hitbox[3])>p.hitbox2[1] and (enemy.hitbox[1]+enemy.hitbox[3])<(p.hitbox2[1]+p.hitbox2[3]):
                enemy.visible=False
                p.hp-=1
                p.health=(p.x,p.y+p.height+3,p.hp*10,5)
    
    #collision between enemy ship's laser and player ship
    for enemy in enemies:
        for bullet in enemy.bullets:
            if bullet.box[0]>=p.hitbox2[0] and (bullet.box[0]+bullet.box[2])<=(p.hitbox2[0]+p.hitbox2[2]) and bullet.visible:
                if (bullet.box[1]+bullet.box[3])>p.hitbox1[1] and (bullet.box[1]+bullet.box[3])<(p.hitbox1[1]+p.hitbox1[3]):
                    bullet.visible=False
                    p.hp-=1
                    p.health=(p.x,p.y+p.height+3,p.hp*10,5)
                if (bullet.box[1]+bullet.box[3])>p.hitbox2[1] and (bullet.box[1]+bullet.box[3])<(p.hitbox2[1]+p.hitbox2[3]):
                    bullet.visible=False
                    p.hp-=1
                    p.health=(p.x,p.y+p.height+3,p.hp*10,5)
            
    #collision between player ship's laser and enemy ship
    for bullet in p.bullets:
        for enemy in enemies:
            if ((bullet.box[0]>=enemy.hitbox[0] and bullet.box[0]<=(enemy.hitbox[0]+enemy.hitbox[2])) or ((bullet.box[0]+bullet.box[2])>=enemy.hitbox[0] and (bullet.box[0]+bullet.box[2])<=(enemy.hitbox[0]+enemy.hitbox[2]))) and enemy.visible:
                if bullet.box[1]>enemy.hitbox[2] and bullet.box[1]<(enemy.hitbox[1]+enemy.hitbox[3]):
                    p.bullets.pop(p.bullets.index(bullet))
                    enemy.visible=False
                    p.score+=enemy.score
                    #to increase the level of overall game for each 100 point scored
                    if p.score%100==0 and p.score!=0:
                        p.live+=1
                        if t1>1000:
                            t1-=500
                            t2-=500
                        if FPSTIMER>3000:
                            FPSTIMER-=200
                        for enemy in enemies:
                            if enemy.vel<2:
                                enemy.vel+=0.1

    #if the enemy ship go over the other side of the map, player ship lose one health
    for enemy in enemies:
        if enemy.visible:
            if enemy.hitbox[1]>1080:
                enemies.pop(enemies.index(enemy))
                enemy.visible=False
                p.hp-=1
                p.health=(p.x,p.y+p.height+3,p.hp*10,5)

#redraw and update the screen
def redraw(p,enemies):
    win.blit(bg,(0,0))
    #move our character and draw it
    p.action()
    p.draw()
    font=pygame.font.SysFont('cosmicans',35,True,True)
    s=font.render('SCORE: {}'.format(str(p.score)),1,(255,0,0))
    l=font.render('LIVE: {}'.format(str(p.live)),1,(255,0,0))
    win.blit(l,(0,0))
    win.blit(s,(1500,0))
    #move the nemy and draw it
    for enemy in enemies:
        enemy.action()
        if enemy.visible:
            enemy.draw()
        elif enemy.visible==False:
            enemies.pop(enemies.index(enemy))
    #update the game display
    pygame.display.update()

#main function
def main():
    t1=2000
    t2=4000
    FPSTIMER=5000
    #increase FPS every 5 second, in another word overall speed of the game
    pygame.time.set_timer(pygame.USEREVENT+1,FPSTIMER)
    #generate an enemy every 2~4 second
    pygame.time.set_timer(pygame.USEREVENT+2,random.randint(t1,t2))
    run = True
    clock=pygame.time.Clock()
    FPS=30
    enemies=[]
    p=Player(850,950,100,90)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
            if event.type==pygame.USEREVENT+1:
                FPS+=1
            if  event.type==pygame.USEREVENT+2:
                generate_enemies(enemies)
        #so that instead of multiple bullets,single bullet wull be shot whenever a spacebar is pressed
        if p.shootcount>0:
            p.shootcount+=1
        if p.shootcount>10:
            p.shootcount=0
        for enemy in enemies:
            if enemy.y>0:
                if enemy.shootcount>0:
                    enemy.shootcount+=1
                if enemy.shootcount>250:
                    enemy.shootcount=0
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            p.up=True
            p.stay=False
        if keys[pygame.K_DOWN]:
            p.down=True
            p.stay=False
        if keys[pygame.K_LEFT]:
            p.left=True
            p.stay=False
        if keys[pygame.K_RIGHT]: 
            p.right=True
            p.stay=False
        if keys[pygame.K_SPACE]:
            p.shoot=True
        p.stay=True

        if p.live==0:
            run =False 
        collide(p,enemies,t1,t2,FPSTIMER)
        redraw(p,enemies)

def main_menu():
    title=pygame.font.SysFont('cosmicans',50,True,True)
    run=True
    while run:
        win.blit(bg,(0,0))
        text=title.render('PRESSED THE MOUSE TO START GAME',1,(250,0,0))
        win.blit(text,(500,300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()
            


            