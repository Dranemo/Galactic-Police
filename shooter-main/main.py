import pygame
import sys
import math
import time

from game import Game
from settings import Settings
#import the class Enemy from the file enemy.py
from enemy import Enemy
#import the class Spaceship from the file spaceship.py
from spaceship import Spaceship
from screen import *
from affichage import *

#définir une clock
clock = pygame.time.Clock()
FPS = 100




# Define game varibales
scroll = 0
tiles = math.ceil(largeur/bg_largeur) + 1
seconde = time.time()

game = Game()
settings = Settings()

#Boucle de jeu

running = True

while running:

    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(background, (i * bg_largeur + scroll, 0))
        
    # reset scroll
    if abs(scroll) > bg_largeur:
        scroll = 0

    if game.is_playing:
        #Scroll background
        scroll -= 5
    else:
        #Scroll background
        scroll -= 2

    #  ------------------------------------------- Projectiles -------------------------------------------
    #recuperer les projectiles du joueur
    for projectile in game.player.all_projectile:
        projectile.move()

    # appliquer l'ensemble des image de mon groupe de projectile
    game.player.all_projectile.draw(screen)

    #recuperer les projectiles des ennemis
    for enemy in game.all_enemy:
        for projectile in enemy.all_projectile:
            projectile.move()

    # appliquer l'ensemble des image de mon groupe de projectile
        enemy.all_projectile.draw(screen)

    #  ------------------------------------------- Enemy -------------------------------------------
    #recuperer les ennemy
    for enemy in game.all_enemy:
        enemy.forward()
        enemy.update_health_bar(screen) 
        # while enemy.rect.x != 1600:
        #     enemy.spawn()

    # appliquer l'ensemble des image de mon groupe de mosntres
    game.all_enemy.draw(screen)

    #  ------------------------------------------- powerUp -------------------------------------------
    #recuperer les ennemy
    for powerUp in game.player.all_upgrades:
        powerUp.forward()
    game.player.all_upgrades.draw(screen)


     #  ------------------------------------------- Game Related -------------------------------------------
    #vérifier si le jeu a commencé ou non
    if (game.is_playing and game.mode_is_choose):
        #déclencher les isntructions de la partie
        game.update(screen, seconde)
    #---------settings--------#
    elif(settings.is_settings):
        show_settings()
    #verifier quelles sont les settings lancés
    elif(settings.is_gameplay):
        show_gameplay()
    elif(settings.is_audio):
        show_audio()
    elif(settings.is_commandes):
        show_commandes()
        
    #Show the screen with the difficulties
    elif(not game.is_playing and not game.mode_is_choose and game.planete_is_choose):
        show_planetes()

    #vérifier si notre jeu n'a pas commencé
    #Show the screen with the difficulties
    elif(not game.is_playing and game.mode_is_choose):
        show_difficulty()
    #vérifier si notre jeu n'a pas commencé
    else:
        show_menu()

    #Dessin de la fenêtre
    pygame.display.flip()

    # Faire spawn des ennemis
    if game.is_playing == True:
        if time.time() > seconde + 3:
            game.spawn_monster()
            seconde = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Fermeture du jeu")
            sys.exit()
       

        if event.type == pygame.KEYDOWN and game.is_playing == True:
            game.pressed[event.key] = True

            #détecter si la touche espace est enclenchée pour lance notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif (event.type == pygame.MOUSEBUTTONDOWN):

            #vérification pour svaoir si la souris est en collision avec le bouton
            if (play_button_rect.collidepoint(event.pos)):

                game.show_planetes()

            #vérification pour svaoir si la souris est en collision avec le bouton
            elif (settings_button_rect.collidepoint(event.pos)):
                settings.show_settings()
            elif(Gameplay_button_rect.collidepoint(event.pos)):
                settings.show_gameplay()
            elif(audio_button_rect.collidepoint(event.pos)):
                settings.show_audio()
            elif(controle_button_rect.collidepoint(event.pos)):
                settings.show_commandes()
            elif(return_button_rect.collidepoint(event.pos)):
                settings.back_settings()
            
            elif (terre_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete1_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete2_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete3_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete4_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete5_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            elif (planete6_button_rect.collidepoint(event.pos)):
                game.show_game_modes()
            
            elif (easy_button_rect.collidepoint(event.pos)):
                game.create_player(1)
                game.start()

            elif (medium_button_rect.collidepoint(event.pos)):
                game.create_player(1.5)

                game.start()
            elif (hard_button_rect.collidepoint(event.pos)):
                game.create_player(2)

                game.start()
            elif (nightmare_button_rect.collidepoint(event.pos)):
                game.create_player(3)

                game.start()
                
                #mettre le jeu en monde "lancé"
                

           
    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)  
