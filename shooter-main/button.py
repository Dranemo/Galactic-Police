import pygame
import math
from screen import screen


#=====================================================================================================================#
#--------------------------------------------------------PLAY---------------------------------------------------------#
#=====================================================================================================================#

#importer charger notre bouton pour lancer la partie 
play_button = pygame.image.load('PygameAssets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/2.7)
play_button_rect.y = math.ceil(screen.get_height()/1.7)

#=====================================================================================================================#
#------------------------------------------------------SETTINGS-------------------------------------------------------#
#=====================================================================================================================#

#importer charger notre bouton pour lancer les settings
settings_button = pygame.image.load('PygameAssets/button-settings.png')
settings_button = pygame.transform.scale(settings_button, (50, 50))
settings_button_rect = settings_button.get_rect()
settings_button_rect.x = math.ceil(screen.get_width()/100)
settings_button_rect.y = math.ceil(screen.get_height()/100)
#gameplay pas selectionné
Gameplay_button = pygame.image.load('PygameAssets/Gameplay.png')
Gameplay_button = pygame.transform.scale(Gameplay_button, (200, 150))
Gameplay_button_rect = Gameplay_button.get_rect()
Gameplay_button_rect.x = math.ceil(screen.get_width()/10.15)
Gameplay_button_rect.y = math.ceil(screen.get_height()/4)
#audio pas selectionné
audio_button = pygame.image.load('PygameAssets/audio.png')
audio_button = pygame.transform.scale(audio_button, (200, 150))
audio_button_rect = audio_button.get_rect()
audio_button_rect.x = math.ceil(screen.get_width()/2.25)
audio_button_rect.y = math.ceil(screen.get_height()/4)
#commandes pas selectionné
controle_button = pygame.image.load('PygameAssets/controle.png')
controle_button = pygame.transform.scale(controle_button, (200, 150))
controle_button_rect = controle_button.get_rect()
controle_button_rect.x = math.ceil(screen.get_width()/1.3)
controle_button_rect.y = math.ceil(screen.get_height()/4)
#bouton retour
return_button = pygame.image.load('PygameAssets/retour.png')
return_button = pygame.transform.scale(return_button, (100, 100))
return_button_rect = return_button.get_rect()
return_button_rect.x = math.ceil(screen.get_width()/100)
return_button_rect.y = math.ceil(screen.get_height()/100)
#gameplay pas selectionné
Gameplay_underline_button = pygame.image.load('PygameAssets/Gameplay_underline.png')
Gameplay_underline_button = pygame.transform.scale(Gameplay_underline_button, (200, 150))
Gameplay_underline_button_rect = Gameplay_underline_button.get_rect()
Gameplay_underline_button_rect.x = math.ceil(screen.get_width()/10.15)
Gameplay_underline_button_rect.y = math.ceil(screen.get_height()/4)
#audio pas selectionné
audio_underline_button = pygame.image.load('PygameAssets/audio_underline.png')
audio_underline_button = pygame.transform.scale(audio_underline_button, (200, 150))
audio_underline_button_rect = audio_underline_button.get_rect()
audio_underline_button_rect.x = math.ceil(screen.get_width()/2.25)
audio_underline_button_rect.y = math.ceil(screen.get_height()/4)
#commandes pas selectionné
controle_underline_button = pygame.image.load('PygameAssets/controle_underline.png')
controle_underline_button = pygame.transform.scale(controle_underline_button, (200, 150))
controle_underline_button_rect = controle_underline_button.get_rect()
controle_underline_button_rect.x = math.ceil(screen.get_width()/1.3)
controle_underline_button_rect.y = math.ceil(screen.get_height()/4)


#=====================================================================================================================#
#------------------------------------------------------PLANETES-------------------------------------------------------#
#=====================================================================================================================#

#importer charger notre bouton pour lancer la planète terre
terre_button = pygame.image.load('PygameAssets/terre.png')
terre_button = pygame.transform.scale(terre_button, (300, 300))
terre_button_rect = terre_button.get_rect()
terre_button_rect.x = math.ceil(screen.get_width()/1.5)
terre_button_rect.y = math.ceil(screen.get_height()/2.50)

#importer charger notre bouton pour lancer la planète 1
planete1_button = pygame.image.load('PygameAssets/planete1.png')
planete1_button = pygame.transform.scale(planete1_button, (200, 200))
planete1_button_rect = planete1_button.get_rect()
planete1_button_rect.x = math.ceil(screen.get_width()/2)
planete1_button_rect.y = math.ceil(screen.get_height()/1.5)

#importer charger notre bouton pour lancer la planète 2
planete2_button = pygame.image.load('PygameAssets/planete2.png')
planete2_button = pygame.transform.scale(planete2_button, (250, 250))
planete2_button_rect = planete2_button.get_rect()
planete2_button_rect.x = math.ceil(screen.get_width()/1.80)
planete2_button_rect.y = math.ceil(screen.get_height()/7.5)

#importer charger notre bouton pour lancer la planète 3
planete3_button = pygame.image.load('PygameAssets/planete3.png')
planete3_button = pygame.transform.scale(planete3_button, (200, 200))
planete3_button_rect = planete3_button.get_rect()
planete3_button_rect.x = math.ceil(screen.get_width()/2.5)
planete3_button_rect.y = math.ceil(screen.get_height()/3)

#importer charger notre bouton pour lancer la planète 4
planete4_button = pygame.image.load('PygameAssets/planete4.png')
planete4_button = pygame.transform.scale(planete4_button, (450, 300))
planete4_button_rect = planete4_button.get_rect()
planete4_button_rect.x = math.ceil(screen.get_width()/8)
planete4_button_rect.y = math.ceil(screen.get_height()/1.5)

#importer charger notre bouton pour lancer la planète 5
planete5_button = pygame.image.load('PygameAssets/planete5.png')
planete5_button = pygame.transform.scale(planete5_button, (175, 175))
planete5_button_rect = planete5_button.get_rect()
planete5_button_rect.x = math.ceil(screen.get_width()/1.20)
planete5_button_rect.y = math.ceil(screen.get_height()/8.5)

#importer charger notre bouton pour lancer la planète 6
planete6_button = pygame.image.load('PygameAssets/planete6.png')
planete6_button = pygame.transform.scale(planete6_button, (150, 150))
planete6_button_rect = planete6_button.get_rect()
planete6_button_rect.x = math.ceil(screen.get_width()/1.25)
planete6_button_rect.y = math.ceil(screen.get_height()/1.25)


#=====================================================================================================================#
#---------------------------------------------------DIFFICULTIES------------------------------------------------------#
#=====================================================================================================================#

#importer charger notre bouton pour lancer le mode easy
easy_button = pygame.image.load('PygameAssets/easy-button.png')
easy_button = pygame.transform.scale(easy_button, (500, 150))
easy_button_rect = easy_button.get_rect()
easy_button_rect.x = math.ceil(screen.get_width()/3)
easy_button_rect.y = math.ceil(screen.get_height()/6)

#importer charger notre bouton pour lancer le mode medium
medium_button = pygame.image.load('PygameAssets/medium-button.png')
medium_button = pygame.transform.scale(medium_button, (500, 150))
medium_button_rect = medium_button.get_rect()
medium_button_rect.x = math.ceil(screen.get_width()/3)
medium_button_rect.y = math.ceil(screen.get_height()/3)

#importer charger notre bouton pour lancer le mode hard
hard_button = pygame.image.load('PygameAssets/hard-button.png')
hard_button = pygame.transform.scale(hard_button, (500, 150))
hard_button_rect = hard_button.get_rect()
hard_button_rect.x = math.ceil(screen.get_width()/3)
hard_button_rect.y = math.ceil(screen.get_height()/2)

#importer charger notre bouton pour lancer le mode hard
nightmare_button = pygame.image.load('PygameAssets/nightmare-button.png')
nightmare_button = pygame.transform.scale(nightmare_button, (500, 150))
nightmare_button_rect = nightmare_button.get_rect()
nightmare_button_rect.x = math.ceil(screen.get_width()/3)
nightmare_button_rect.y = math.ceil(screen.get_height()/1.5)