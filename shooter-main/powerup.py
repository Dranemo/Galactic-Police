import pygame
import random

class PowerUp(pygame.sprite.Sprite):

    def __init__(self, enemy, type):
        super().__init__()
        self.type = type
        self.enemy = enemy

        if self.type == 0:
            self.image = pygame.image.load('PygameAssets/h.png') #Heal
        elif self.type == 1:
            self.image = pygame.image.load('PygameAssets/c.png') #Upgrade vaisseau
        elif self.type == 2:
            self.image = pygame.image.load('PygameAssets/s.png') #Multiplicateur de score

        self.image = pygame.transform.scale(self.image, (50,50))

        self.rect = self.image.get_rect()
        self.rect.x = self.enemy.rect.x
        self.rect.y = self.enemy.rect.y

        self.speed = random.randint(1,3)

    def remove(self):
        self.enemy.game.player.all_upgrades.remove(self)



    def forward(self):
        self.rect.x -= self.speed

        if self.rect.x < -50:
            self.remove()


        for player in self.enemy.game.check_collision(self, self.enemy.game.all_players):
            if self.type == 0:
                player.hp = player.max_hp
                self.remove()
            elif self.type == 1:
                player.upgrade += 1
                player.upgrade_ship()
                self.remove()
            elif self.type == 2:
                self.remove()