import pygame
import math

#Initialisation des dimensions de la fenêtre
largeur = 1920
hauteur = 1080

#Initialize Pygame
pygame.init()

#Création de la fenêtre en passant ses dimensions en pixel sous forme d'un tuple
pygame.display.set_caption("Shoot'em up")
screen = pygame.display.set_mode((largeur,hauteur))

#importer de charger l'arrière plan de notre jeu
background = pygame.image.load('PygameAssets/bgspace.jpg')
bg_largeur = 1920
bg_hauteur = 1080
background = pygame.transform.scale(background, (bg_largeur, bg_hauteur))

#importer charger notre bannière
banner = pygame.image.load('PygameAssets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/3)