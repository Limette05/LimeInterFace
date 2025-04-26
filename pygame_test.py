import pygame
import sys

pygame.init()
background = pygame.image.load("assets/graphics/background.png")
screen = pygame.display.set_mode([1500,750])
clock = pygame.time.Clock()
pygame.display.set_caption("PyGame Test-Programm")

stehen = pygame.image.load("assets/graphics/player/stand.png")
sprung = pygame.image.load("assets/graphics/player/sprung.png")
rechtsGehen = [pygame.image.load("assets/graphics/player/rechts1.png"),pygame.image.load("assets/graphics/player/rechts2.png"),pygame.image.load("assets/graphics/player/rechts3.png"),pygame.image.load("assets/graphics/player/rechts4.png"),pygame.image.load("assets/graphics/player/rechts5.png"),pygame.image.load("assets/graphics/player/rechts6.png"),pygame.image.load("assets/graphics/player/rechts7.png"),pygame.image.load("assets/graphics/player/rechts8.png")]
linksGehen = [pygame.image.load("assets/graphics/player/links1.png"),pygame.image.load("assets/graphics/player/links2.png"),pygame.image.load("assets/graphics/player/links3.png"),pygame.image.load("assets/graphics/player/links4.png"),pygame.image.load("assets/graphics/player/links5.png"),pygame.image.load("assets/graphics/player/links6.png"),pygame.image.load("assets/graphics/player/links7.png"),pygame.image.load("assets/graphics/player/links8.png")]
sprungsound = pygame.mixer.Sound("assets/sounds/sprung.wav")

class spieler:
    def __init__(self,x,y,speed,breite,hoehe,sprungvar,richtung,schritte_links,schritte_rechts):
        self.x = x
        self.y = y
        self.speed = speed
        self.breite = breite
        self.hoehe = hoehe
        self.sprungvar = sprungvar
        self.richtung = richtung
        self.schritte_links = schritte_links
        self.schritte_rechts = schritte_rechts
        self.sprung = False
    def laufen(self,liste):
        if liste[0]:
            self.x -= self.speed
            self.richtung = [1,0,0,0]
            self.schritte_links += 1
        if liste[1]:
            self.x += self.speed
            self.richtung = [0,1,0,0]
            self.schritte_rechts += 1
    def resetSchritte(self):
        self.schritte_links = 0
        self.schritte_rechts = 0
    def stehen(self):
        self.richtung = [0,0,1,0]
        self.resetSchritte()
    def sprungsetzen(self):
        if self.sprungvar == -16:
            self.sprung = True
            self.sprungvar = 15
            pygame.mixer.Sound.play(sprungsound)
    def springen(self):
        if self.sprung:
            self.richtung = [0,0,0,1]
            if self.sprungvar >= -15:
                n = 1
                if self.sprungvar < 0:
                    n = -1
                self.y -= (self.sprungvar ** 2) * 0.16 * n
                self.sprungvar -= 1
            else:
                self.sprung = False
    def spZeichnen(self):
        if self.schritte_rechts == 63:
            self.schritte_rechts = 0
        if self.schritte_links == 63:
            self.schritte_links = 0

        if self.richtung[0]:
            screen.blit(linksGehen[self.schritte_links // 8], (self.x, self.y))

        if self.richtung[1]:
            screen.blit(rechtsGehen[self.schritte_rechts // 8], (self.x, self.y))

        if self.richtung[2]:
            screen.blit(stehen, (self.x, self.y))

        if self.richtung[3]:
            screen.blit(sprung, (self.x, self.y))

def draw():
    screen.blit(background, (0, 0))
    spieler1.spZeichnen()
    pygame.display.update()

wall_left = pygame.draw.rect(screen, (0,0,0), (0,0,2,755), 0)
wall_right = pygame.draw.rect(screen, (0,0,0), (1499,0,2,755), 0)
spieler1 = spieler(50,425,6,96,128,-16,[0,0,1,0],0,0)
go = True
sprungvar = -16
#crouchvar = 10
# [links,rechts,stand,sprung
richtung = [0,0,0,0]
schritte_rechts = 0
schritte_links = 0
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    player = pygame.Rect(spieler1.x,spieler1.y,96,128)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and not player.colliderect(wall_right):
        spieler1.laufen([0,1])
    elif pressed[pygame.K_LEFT] and not player.colliderect(wall_left):
        spieler1.laufen([1,0])
    else:
        spieler1.stehen()

    if pressed[pygame.K_UP]:
        spieler1.sprungsetzen()
    spieler1.springen()

#    if crouchvar <= 9:
#        n = 1
#        if crouchvar < 0:
#            n = -1
#        y -= (crouchvar**2)*0.17*n
#        hoehe += (crouchvar ** 2) * 0.17 * n
#        breite -= (crouchvar ** 2) * 0.034 * n
#        crouchvar += 1

    draw()
    clock.tick(60)