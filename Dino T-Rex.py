##fonctions

def waitclic():
    """attend un clic sur la fenêtre et renvoie les coordonnées du clic"""
    continuer=1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type == MOUSEBUTTONDOWN:
                return event.pos

def affichage (dino_start):
    """affiche l'écran de départ"""
    screen.blit(dino_start,(50,50))
    #screen.blit(sol,(0,50))
    pygame.display.flip()

def controles(color):
    """gère les contrôles :
        - les touches espace et flèche haut font sauter le dino
        - la touche flèche bas fait s'accroupir le dino
        - cliquer sur la fenêtre lance un caillou sur le dino"""
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            continuer = 0
            exit(0)
        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP:   #sauter
                print ("Pogo!")
                a = 100
                while a > 30:
                    screen.fill(color)
                    screen.blit(dino_metal,(20,a))
                    pygame.display.flip()
                    a = a - 1
                for i in range (20):
                    screen.fill(color)
                    screen.blit(dino_metal,(20,a))
                    pygame.display.flip()
                while a < 100:
                    screen.fill(color)
                    screen.blit(dino_metal,(20,a))
                    pygame.display.flip()
                    a = a + 1

            if event.key == K_DOWN:    #s'accroupir pendant un temps donné
                print ("Ventriglisse!")
                for i in range (3):
                    screen.fill(color)
                    screen.blit(dino_duck1,(20,120))
                    pygame.display.flip()
                    pygame.time.delay(150)
                    screen.fill(color)
                    screen.blit(dino_duck2,(20,120))
                    pygame.display.flip()
                    pygame.time.delay(150)

        if event.type == MOUSEBUTTONDOWN:   #lance un caillou sur le dino
            print ("Aïe!")
            for i in range (2):
                screen.fill(color)
                screen.blit (dino_caillou1,(20,72))
                pygame.display.flip()
                pygame.time.delay(125)
                screen.fill(color)
                screen.blit (dino_caillou2,(20,72))
                pygame.display.flip()
                pygame.time.delay(125)
            screen.blit(dino_start,(20,100))
            pygame.display.flip()
            dinoception()
            pygame.time.delay(500)

def animation(dino_move1,dino_move2,color):
    global posx
    """gère l'animation de marche du dino"""
    screen.fill(color)
    screen.blit(dino_move1,(20,100))
    pygame.display.flip()
    pygame.time.delay(100)
    screen.fill(color)
    screen.blit(dino_move2,(20,100))
    pygame.display.flip()
    pygame.time.delay(100)
    pygame.display.flip()

def dinoception():
    for i in range (100):
        px = randint (0,500)
        py = randint (0,300)
        a = randint (1,9)
        if a == 1:
            screen.blit(dino_start,(px,py))
        if a == 2:
            screen.blit(dino_move1,(px,py))
        if a == 3:
            screen.blit(dino_move2,(px,py))
        if a == 4:
            screen.blit(dino_duck1,(px,py))
        if a == 5:
            screen.blit(dino_duck2,(px,py))
        if a == 6:
            screen.blit(dino_thug,(px,py))
        if a == 7:
            screen.blit(dino_kawaii,(px,py))
        if a == 8:
            screen.blit(dino_piscine,(px,py))
        if a == 9:
            screen.blit(dino_metal,(px,py))
        pygame.display.flip()
        pygame.time.delay(20)



import pygame
from pygame import *

import random
from random import *

pygame.init()

window = pygame.display.set_mode ((500,300))
screen = pygame.display.get_surface ()

##couleurs
white = (255,255,255)
black = (0,0,0)
grey = (150,150,150)

##images
#dino
dino_start = pygame.image.load("dinos/dino_stand.png").convert()
dino_move1 = pygame.image.load("dinos/dino_moving_1.png").convert()
dino_move2 = pygame.image.load("dinos/dino_moving_2.png").convert()
dino_duck1 = pygame.image.load("dinos/dino_duck_1.png").convert()
dino_duck2 = pygame.image.load("dinos/dino_duck_2.png").convert()
dino_caillou1 = pygame.image.load("dinos/dino_caillou_1.png").convert()
dino_caillou2 = pygame.image.load("dinos/dino_caillou_2.png").convert()
dino_thug = pygame.image.load("dinos/dino_thug.png").convert()
dino_kawaii = pygame.image.load("dinos/dino_kawaii.png").convert()
dino_piscine = pygame.image.load("dinos/dino_piscine_beauf.png").convert()
dino_metal = pygame.image.load("dinos/dino_metal.png").convert()

#sol


#cactus


#dinos volants


#suppression du fond
dino_start.set_colorkey ((0,255,0))
dino_move1.set_colorkey ((0,255,0))
dino_move2.set_colorkey ((0,255,0))
dino_duck1.set_colorkey ((0,255,0))
dino_duck2.set_colorkey ((0,255,0))
dino_caillou1.set_colorkey ((0,255,0))
dino_caillou2.set_colorkey ((0,255,0))
dino_thug.set_colorkey ((0,255,0))
dino_kawaii.set_colorkey ((0,255,0))
dino_piscine.set_colorkey ((0,255,0))
dino_metal.set_colorkey ((0,255,0))

##variables globales
#zone dans laquelle le dino est vulnérable
hitbox_dino = (40,44)
hitbox_dino_duck = (42,28)
posx = 500

##musique
#TtFaF = pygame.mixer.music.load("musiques/Through the Fire and Flames.mp3")
#pygame.mixer.music.play()

##programme principal
pygame.key.set_repeat(1,1)

initialisation = 1
while initialisation:
    affichage(dino_start)
    P = waitclic()
    screen.fill(black)
    screen.blit(dino_caillou1,(50,22))
    pygame.display.flip()
    pygame.time.delay(1000)
    screen.fill(black)
    initialisation = 0


continuer = 1
while continuer:
    posy = randint (150,170)
    animation(dino_move1,dino_move2,black)
    controles(black)


pygame.time.delay(2000)
pygame.quit()
exit(0)