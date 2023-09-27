##to do list
#séparer les fonctions en fonctions de calcul et d'affichage : done
#gérer l'affichage du score : done
#faire l'animation de défaite : done
#corriger les bugs de collisions : done
#changer la rng pour avoir plus de cailloux : done
#deux cailloux en meme temps : done
#controles en zqsd : done
##gérer plusieurs  boosts en aléatoire
##bonus de perte de contrôle : à faire
##bonus de super vitesse : a faire

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

def anim_dino_1(dino_pas1,dino_pas2,color):
    """gère la première frame de la marche du dino"""
    global posy
    screen.blit(dino_pas1,(50,posy))
    pygame.display.flip()
    pygame.time.delay(100)
    pygame.display.flip()

def anim_dino_2(dino_pas1,dino_pas2,color):
    """gère la deuxième frame de la marche du dino"""
    global posy
    screen.blit(dino_pas2,(50,posy))
    pygame.display.flip()
    pygame.time.delay(100)
    pygame.display.flip()

def controles(color):
    """gère les contrôles :
        - flèche haut pour monter
        - flèche bas pour descendre"""
    global posy
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            continuer = 0
            exit(0)
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                print("haut")
                pygame.draw.rect(screen,color,((50,posy),(50,50)),0)
                pygame.display.flip()
                if posy > 55:
                    posy = posy - 55
                    print (posy)
                    return posy
            if event.key == K_DOWN or event.key == K_s:
                print("bas")
                pygame.draw.rect(screen,color,((50,posy),(50,50)),0)
                pygame.display.flip()
                if posy < 165:
                    posy = posy + 55
                    print (posy)
                    return posy

def anim_caillou(difficulte):
    global pos_caillou_x
    global pos_caillou_y
    pos_caillou_y = line * 55
    pos_caillou_x = pos_caillou_x - difficulte
    return pos_caillou_x
def anim_caillou2(difficulte):
    global pos_caillou_x2
    global pos_caillou_y2
    pos_caillou_y2 = line2 * 55
    pos_caillou_x2 = pos_caillou_x2 - difficulte
    return pos_caillou_x2

def boost(difficulte):
    global pos_boost_x
    global pos_boost_y
    pos_boost_y = line * 55
    pos_boost_x = pos_boost_x - difficulte
    return pos_boost_x

#définit si l'obstacl est un caillou ou un boost selon la variable 'objet'
def obstacle(difficulte):
    if objet == 1:
        anim_caillou(difficulte)
    if objet == 2:
        boost(difficulte)
def obstacle2(difficulte):
    anim_caillou2(difficulte)


def fond(lxa,lya,lxb,lyb):
    """affiche les lignes du fond"""
    for i in range (5):
        pygame.draw.line(screen,brown_walls,(lxa,lya),(lxb,lyb))
        pygame.display.flip()
        lya = lya + 55
        lyb = lyb + 55
        pygame.time.delay (100)

def affichage():
    """gère l'affichage des images et non les calculs"""
    #rectangle sur l'ancienne position de l'obstacle
    pygame.draw.rect(screen,brown_ground,((pos_caillou_x,pos_caillou_y),(600,50)),0)
    pygame.draw.rect(screen,brown_ground,((pos_boost_x,pos_boost_y),(600,50)),0)
    pygame.draw.rect(screen,brown_ground,((pos_caillou_x2,pos_caillou_y2),(600,50)),0)
    #rectangle sur l'ancienne position du dino
    pygame.draw.rect(screen,brown_ground,((50,posy),(50,50)),0)
    #affichage de l'obstacle
    screen.blit(caillou,(pos_caillou_x,pos_caillou_y))
    screen.blit(boost_obstacle,(pos_boost_x,pos_boost_y))
    screen.blit(caillou2,(pos_caillou_x2,pos_caillou_y2))
    #affichage du dino1
    anim_dino_1(dino_pas1,dino_pas2,brown_ground)
    pygame.display.flip()
    #réaffichage des rectangles et de l'obstacle
    pygame.draw.rect(screen,brown_ground,((pos_caillou_x,pos_caillou_y),(600,50)),0)
    pygame.draw.rect(screen,brown_ground,((pos_boost_x,pos_boost_y),(600,50)),0)
    pygame.draw.rect(screen,brown_ground,((50,posy),(50,50)),0)
    pygame.draw.rect(screen,brown_ground,((pos_caillou_x2,pos_caillou_y2),(600,50)),0)
    screen.blit(caillou,(pos_caillou_x,pos_caillou_y))
    screen.blit(boost_obstacle,(pos_boost_x,pos_boost_y))
    screen.blit(caillou2,(pos_caillou_x2,pos_caillou_y2))
    #affichage du dino2
    anim_dino_2(dino_pas1,dino_pas2,brown_ground)
    pygame.display.flip()

def affichage_texte(font,texte,couleur,pos):
    text = font.render(texte,1,couleur)
    screen.blit(text,(pos))
    pygame.display.flip()

def collision(posy,pos_caillou_x,pos_caillou_y,pos_caillou_x2,pos_caillou_y2):
    global collide
    global boost_var
    global dino_pas1
    global dino_pas2
    global caillou
    global caillou2
    global num_score
    #print (collide)
    if 79 - difficulte < pos_caillou_x < 80:
        if dino_pas1 == dino_metal1:
            if posy == pos_caillou_y:
                boost_var = 0
                dino_pas1 = dino_move1
                dino_pas2 = dino_move2
                caillou = caillou_obstacle_broken
                num_score = num_score + 100
                return dino_pas1,dino_pas2,posy,num_score,boost_var,caillou
            if posy == pos_caillou_y2:
                boost_var = 0
                dino_pas1 = dino_move1
                dino_pas2 = dino_move2
                caillou2 = caillou_obstacle_broken
                num_score = num_score + 100
                return dino_pas1,dino_pas2,posy,num_score,boost_var,caillou2
        if posy == pos_caillou_y or posy == pos_caillou_y2:
            print ("Paf!")
            collide = 0
            return collide
    if 79 - difficulte < pos_boost_x < 80:
        if posy == pos_boost_y:
            print ("Boost!")
            posy = posy + 10
            boost_var = 1
            dino_pas1 = dino_metal1
            dino_pas2 = dino_metal2
            return dino_pas1,dino_pas2,posy,boost_var

##importation des modules
#pygame
import pygame
from pygame import *
#random
import random
from random import *

##initialisation
pygame.init()

##création de la fenêtre
window = pygame.display.set_mode ((600,375))
screen = pygame.display.get_surface ()

##couleurs
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (150,150,150)
brown_ground = (237,190,82)
brown_walls = (175,143,106)

##variables globales
posy = 110
#définition de l'objet
objet = 0
#définition de la variable boost : 0 si aucun boost actif, 1 si un boost est actif
boost_var = 0
#coordonnées de l'obstacle caillou
pos_caillou_x = 600
pos_caillou_y = 0
pos_caillou_x2 = 600
pos_caillou_y2 = 55
#coordonnées du boost
pos_boost_x = 600
pos_boost_y = 0
#coordonnées pour les lignes du fond
lignexa = 0
ligneya = 53
lignexb = 600
ligneyb = 53
#lignes sur lesquelles se trouvent les objets
line = 2
line2 = 1
#variables en lien avec la difficulté
difficulte = 15
disp_diff = str(difficulte)
#polices d'écriture
font = pygame.font.SysFont("Sans-Serif",100,bold = False,italic = False,constructor = None)
font60 = pygame.font.SysFont("Sans-Serif",45,bold = False,italic = False,constructor = None)
font10 = pygame.font.SysFont("Courrier",30,bold = False,italic = False,constructor = None)

#textes
    #score
num_score = 0
score = str(num_score)
    #nom
nom_jeu = "Dino T-Rex The Game 2000 Turbo XP"

##images
    ##écrans
#écran de départ
start_screen = pygame.image.load("ecrans/start screen.png").convert()
#écran de fin avec "rejouer" et "quitter"
end_screen = pygame.image.load("ecrans/end_screen.png").convert()

    ##dinos
#dino de départ
dino_start = pygame.image.load("dinos/dino_stand.png").convert()
#marche du dino
dino_move1 = pygame.image.load("dinos/dino_moving_1.png").convert()
dino_move2 = pygame.image.load("dinos/dino_moving_2.png").convert()
#dino accroupi
dino_duck1 = pygame.image.load("dinos/dino_duck_1.png").convert()
dino_duck2 = pygame.image.load("dinos/dino_duck_2.png").convert()
#dino frappé par le caillou
dino_caillou1 = pygame.image.load("dinos/dino_caillou_1.png").convert()
dino_caillou2 = pygame.image.load("dinos/dino_caillou_2.png").convert()
#dino avec des lunettes de soleil
dino_thug = pygame.image.load("dinos/dino_thug.png").convert()
#dino tout kawaii UwU
dino_kawaii = pygame.image.load("dinos/dino_kawaii.png").convert()
#dino avec un maillot de bain adidas
dino_piscine = pygame.image.load("dinos/dino_piscine_beauf.png").convert()
#dino metalleu
dino_metal = pygame.image.load("dinos/dino_metal.png").convert()
dino_metal1 = pygame.image.load("dinos/dino_metal_1.png").convert()
dino_metal2 = pygame.image.load("dinos/dino_metal_2.png").convert()
#dino qui dort a la fin
dino_ded1 = pygame.image.load("dinos/dino_ded_1.png").convert()
dino_ded2 = pygame.image.load("dinos/dino_ded_2.png").convert()

    ##obstacles
#caillou
caillou_obstacle = pygame.image.load("obstacles/caillou.png").convert()
caillou_obstacle_broken = pygame.image.load("obstacles/caillou_broken.png").convert()
#boost
boost_obstacle = pygame.image.load("obstacles/boost.png").convert()

##suppression du fond de l'image
#dinos
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
dino_metal1.set_colorkey ((0,255,0))
dino_metal2.set_colorkey ((0,255,0))
dino_ded1.set_colorkey ((0,255,0))
dino_ded2.set_colorkey ((0,255,0))
#obstacles
caillou_obstacle.set_colorkey ((0,255,0))
caillou_obstacle_broken.set_colorkey ((0,255,0))

##affectation des images aux variables
dino_pas1 = dino_move1
dino_pas2 = dino_move2
caillou = caillou_obstacle
caillou2 = caillou_obstacle

##tableaux pour anims de dino
dino_ded_anim1 = [dino_ded1,dino_ded2]

##initialisation
initialisation = 1
while initialisation:
    screen.blit(start_screen,(0,0))
    screen.blit(dino_start,(280,155))
    pygame.display.flip()
    P = waitclic()
    screen.fill(brown_ground)
    pygame.display.flip()
    fond(lignexa,ligneya,lignexb,ligneyb)
    initialisation = 0

##boucle totale
#sert a relancer le programme si on veut rejouer sans avoir a quitter la fenetre /!\ : in progress
continuer = 1
while continuer:
    line = 2
    line2 = 1
    objet = 1
    # print ("ligne : ",line)
    # print ("objet : ",objet)
    # print ("difficulté : ",difficulte)
    collide = 1
    while pos_caillou_x > 0:
        while collide:
            # print (line2)
            controles(brown_ground)
            collision(posy,pos_caillou_x,pos_caillou_y,pos_caillou_x2,pos_caillou_y2)
            affichage_texte(font60,nom_jeu,black,(5,5))
            pygame.draw.rect(screen,brown_ground,((0,230),(600,350)),0)
            affichage_texte(font,score,black,(10,230))
            disp_diff = str(difficulte)
            affichage_texte(font60,disp_diff,black,(10,300))
            affichage()
            obstacle(difficulte)
            obstacle2(difficulte)
            num_score = num_score + 1
            score = str(num_score)
            if pos_caillou_x < (0 - difficulte) or pos_boost_x < (0 - difficulte):
                line = randint(1,3)
                if line == 1:
                    line2 = randint(2,3)
                if line == 3:
                    line2 = randint(1,2)
                if line == 2:
                    line2 = randint(1,3)
                if boost_var == 1:
                    objet = 1
                else:
                    objet = randint(1,2)
                print ("line",line,"line2",line2)
                pos_caillou_x = 600
                pos_caillou_x2 = 600
                pos_boost_x = 600
                num_score = num_score + 10
                difficulte = difficulte + 1
                caillou = caillou_obstacle
                caillou2 = caillou_obstacle
                pygame.draw.rect(screen,brown_ground,((0,pos_caillou_y),(600,50)),0)
                pygame.draw.rect(screen,brown_ground,((0,pos_caillou_y2),(600,50)),0)
                pygame.draw.rect(screen,brown_ground,((0,pos_boost_y),(600,50)),0)
        # print("Game Over!")
        pos_caillou_x = -50
        pos_caillou_x2 = -50
    pygame.time.delay(10)
    continuer = 0

##animation de défaite
defaite = 1
while defaite:
    screen.fill(black)
    for i in range (5):
        a = 0 - (30 * i)
        a2 = 80 - (30 * i)
        py = randint (posy,posy + 40)
        py2 = randint (posy + 40,posy + 80)
        for i in range (6):
            pygame.draw.line(screen,red,(a,py),(a2,py2))
            screen.blit(caillou_obstacle,(110,posy))
            screen.blit(dino_caillou1,(80,posy))
            affichage_texte(font10,"cheh!",white,(150,posy))
            pygame.display.flip()
            pygame.time.delay (20)
            py = randint (posy,posy + 60)
            a = a + 80
            a2 = a2 + 80
            pygame.draw.line(screen,red,(a,py2),(a2,py))
            pygame.display.flip()
            pygame.time.delay(20)
            py2 = randint (posy + 20,posy + 80)
            a = a + 80
            a2 = a2 + 80
    pygame.time.delay(2000)
    defaite = 0

##affichage du score après la défaite
fin = 1
while fin:
    screen.fill(brown_walls)
    pygame.display.flip()
    affichage_texte(font60,"Game Over",black,(10,10))
    affichage_texte(font,"Score : ",black,(10,150))
    affichage_texte(font,score,black,(260,150))
    affichage_texte(font,"Level : ",black,(10,225))
    affichage_texte(font,disp_diff,black,(240,225))
    score_total = num_score * difficulte
    total_txt = str(score_total)
    affichage_texte(font,"Total : ",black,(10,300))
    affichage_texte(font,total_txt,black,(250,300))
    pygame.display.flip()
    P = waitclic()
    fin = 0

##affichage du score dans le shell
print ("score :",score)
print ("niveau :",difficulte)
print ("total :",num_score * difficulte)

##fin du programme et fermeture de la fenêtre
print ("fin!")
pygame.time.delay(1000)
pygame.quit()
exit(0)