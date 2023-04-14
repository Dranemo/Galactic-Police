import pygame
import random
import time
from projectile import Projectile
from powerup import PowerUp

#Classe des ennemis
class Enemy(pygame.sprite.Sprite):

    def __init__(self, game, type, difficulty):
        super().__init__()
        self.game = game
        self.type = type
        self.difficulty = difficulty

        self.spawned = False

        if type == 0:
            self.hp = 100 * self.difficulty
            self.max_hp = 100 * self.difficulty
            self.speed = 2 * self.difficulty
            self.attack = 20 * self.difficulty
            self.image = pygame.image.load('PygameAssets/asteroid.png')
            self.image = pygame.transform.scale(self.image, (200,184))
        elif type == 1:
            self.hp = 25 * self.difficulty
            self.max_hp = 25 * self.difficulty
            self.speed = 0 * self.difficulty
            self.attack = 200 * self.difficulty
            self.image = pygame.image.load('PygameAssets/ship_gun_enemy.png')
            self.image = pygame.transform.scale(self.image, (200,75))




        self.all_projectile = pygame.sprite.Group()
        # self.image = pygame.transform.scale(self.image, (1200,1200))
        self.rect = self.image.get_rect()
        self.projectileHit = 0
        self.destroy = time.time()

        self.rect.x = 2300
        # self.rect.x = 1600
        self.rect.y = random.randint(0, 900)

        self.launch = time.time()




# idée : changer la couleur de la barre en fonction de l'environnement
    def update_health_bar(self, surface):
        #definir la couleur de la jauge de vie
        bar_color = (255, 0, 0) #rouge
        #definir une couleur pour l'arriere plan de la jauge
        back_bar_color = (60, 60, 60)

        #definir la position de la jauge de vie + largeur+ epaisseur
        hp = (self.hp / self.max_hp) * 200
        bar_position = [self.rect.x, self.rect.y - 20, hp, 10]
        #definir la positiond e l'arrere plan de la jauge
        back_bar_position = [self.rect.x, self.rect.y - 20, 200, 10]

        #dessine la bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        

    def remove(self, drop):
        # Est ce que drop de powerup ou non + determination de laquelle
        if drop == True:
            powerup_ornot = random.randint(0, 2*(self.difficulty*2))
            if powerup_ornot == 0:
                if self.game.player.hp == self.game.player.max_hp:
                    powerup = random.randint(1, 2)
                elif self.game.player.upgrade == 6:
                    powerup = 2
                else:
                    powerup = random.randint(0,2)
                self.spawnPowerup(powerup)
        # self.spawnPowerup(1)
        self.game.all_enemy.remove(self)

    def spawnPowerup(self, type):
        self.game.player.all_upgrades.add(PowerUp(self, type))


    # Spawn
    def spawn(self):
        if self.type == 1 and self.rect.x > 1604:
            self.rect.x -= 5
        else:
            self.spawned = True
        if self.type == 0 and self.rect.x < 1900:
            self.spawned = True
        
    # Sort de l'écran apres etre trop resté
    def gone(self):
        self.rect.x += 10
        self.rect.y -= 5
        if self.rect.y < -200 or self.rect.x > 2100:
            self.remove(False)

    # Prend des dégâts
    def damage(self, amount):
        if (self.hp - amount < amount) :
            self.remove(True)
        else:
            self.hp -= amount

    def launch_projectile(self):
        self.all_projectile.add(Projectile(self.game.player, self, 1, 0))

    def forward(self):


        #mets des degats aux joueurs si collision et supprime l'ennemi
        if self.game.check_collision(self, self.game.all_players):
            self.remove(False)
            self.game.player.damage(self.attack)
        else:
            self.spawn()
            self.rect.x -= self.speed

        # fais disparaitre les ennemis hors de l'ecran
        if self.rect.x < -200:
            self.remove(False)

        # fait disparaitre les ennemis fixes
        if self.destroy + 10 < time.time() and self.type == 1:
            self.gone()

        # Tirer des missiles
        if self.type == 1 and self.rect.x == 1600:
            if self.launch + 2/self.difficulty <= time.time():
                self.launch_projectile()
                self.launch = time.time()
