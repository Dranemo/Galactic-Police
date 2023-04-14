from screen import *
from button import * 


def show_planetes():

    screen.blit(terre_button, terre_button_rect)
    screen.blit(planete1_button, planete1_button_rect)
    screen.blit(planete2_button, planete2_button_rect)
    screen.blit(planete3_button, planete3_button_rect)
    screen.blit(planete4_button, planete4_button_rect)
    screen.blit(planete5_button, planete5_button_rect)
    screen.blit(planete6_button, planete6_button_rect)

def show_settings():
    screen.blit(Gameplay_button, Gameplay_button_rect)
    screen.blit(audio_button, audio_button_rect)
    screen.blit(controle_button, controle_button_rect)
    screen.blit(return_button, return_button_rect)

def show_gameplay():
    screen.blit(Gameplay_underline_button, Gameplay_underline_button_rect)
    screen.blit(audio_button, audio_button_rect)
    screen.blit(controle_button, controle_button_rect)
    screen.blit(return_button, return_button_rect)

def show_audio():
    screen.blit(Gameplay_button, Gameplay_underline_button_rect)
    screen.blit(audio_underline_button, audio_button_rect)
    screen.blit(controle_button, controle_button_rect)
    screen.blit(return_button, return_button_rect)

def show_commandes():
    screen.blit(Gameplay_button, Gameplay_underline_button_rect)
    screen.blit(audio_button, audio_button_rect)
    screen.blit(controle_underline_button, controle_button_rect)
    screen.blit(return_button, return_button_rect)

def show_menu():
    screen.blit(banner, banner_rect)
    screen.blit(play_button, play_button_rect)
    screen.blit(settings_button, settings_button_rect)

def show_difficulty():
    screen.blit(easy_button, easy_button_rect)
    screen.blit(medium_button, medium_button_rect)
    screen.blit(hard_button, hard_button_rect)
    screen.blit(nightmare_button, nightmare_button_rect)