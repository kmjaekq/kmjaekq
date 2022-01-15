from pygame import *
font.init()
window=display.set_mode((700,500))
display.set_caption("Пинг-Понг")
background = transform.scale(
        image.load("a.jpg"),
        (700,500)
)
clock=time.Clock()
FPS=60 
score=0
lost=0
finish=True
game=True
class GameSprite(sprite.Sprite):
        def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
                super().__init__()
                self.image = transform.scale(image. load(player_image), (size_x, size_y))
                self. speed = player_speed
                self.rect = self.image.get_rect()
                self.rect.x = player_x
                self.rect.y = player_y
        def reset(self):
                window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y> 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y< 500-80:
            self.rect.y+=self.speed
    def update1(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_w] and self.rect.y> 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y< 500-80:
            self.rect.y+=self.speed


player1=Player("ad.jpg",0,100,100,100,10)
player2=Player("ad.jpg",600,100,100,100,10)
player3=Player("ada.jpg",350,50,100,100,10)
finish=False
run=True
speed_x = 3
speed_y=3

score1=0
font1=font.Font(None,70)
zzz=font1.render("Score1:",True,(255,215,0))

score2=0
font2=font.Font(None,70)
xxx=font1.render("Score2:",True,(200,100,10))

font3=font.Font(None,70)
www=font3.render("Игра окончена",True,(200,200,50))

while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
    if finish !=True:
        player3.rect.x+=speed_x
        player3.rect.y+=speed_y
        if player3.rect.y>500-50 or player3.rect.y<0:
            speed_y*=-1
        if sprite.collide_rect(player1,player3):
            speed_x*=-1
        if sprite.collide_rect(player2,player3):
            speed_x*=-1
        if player3.rect.x>700:
            score2+=1
            player3.rect.x=350
            player3.rect.y=50
   
        if player3.rect.x<0:
            score1+=1
            player3.rect.x=350
            player3.rect.y=50
        ddd=font1.render(str(score1),True,(255,215,0))
        vvv=font1.render(str(score2),True,(200,100,10))
        window.blit(background,(0,0))
        window.blit(zzz,(200,0))
        window.blit(xxx,(200,30))
        window.blit(ddd,(400,0))
        window.blit(vvv,(400,30))
        
        player1.update()
        player2.update1()
        
        display.update()
        player1.reset()
        player2.reset()
        player3.reset()
    if score1==10 or score2==10:
        finish=True
        font3=font.Font(None,70)
        www=font3.render("Игра окончена",True,(200,200,50))
        window.blit(www,(200,60))
    display.update()
    clock.tick(FPS)

