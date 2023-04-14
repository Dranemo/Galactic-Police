import pygame

#definir la classe qui va gerer les projectiles

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, enemy, who, level):
        super().__init__()
        self.target = who #qui lance ? 1 = enemy / 0 = player
        self.level = level #le niveau de l'upgrade, 0 = enemi
        self.speed = 15
        self.player = player
        self.enemy = enemy
        self.damage = 15
        if self.target == 0:
            if self.level == 1:
                self.image = pygame.image.load('PygameAssets/little_purple_beam.png')
            elif self.level == 2:
                self.image = pygame.image.load('PygameAssets/purple_beam.png')
            elif self.level == 3:
                self.image = pygame.image.load('PygameAssets/blue_beam.png')
            elif self.level == 4:
                self.image = pygame.image.load('PygameAssets/cyan_beam.png')
            elif self.level == 5:
                self.image = pygame.image.load('PygameAssets/cyan_ball2.png')
            elif self.level >= 6:
                self.image = pygame.image.load('PygameAssets/cyan_ball1.png')
            self.rect = self.image.get_rect()
            self.rect.x = player.rect.x + 120
            self.rect.y = player.rect.y + 80
        elif self.target == 1:
            self.image = pygame.image.load('PygameAssets/red_beam.png')
            self.rect = self.image.get_rect()
            self.rect.x = enemy.rect.x - 30
            self.rect.y = enemy.rect.y + 30

    def remove(self):
        if self.target == 0:
            self.player.all_projectile.remove(self)
        if self.target == 1:
            self.enemy.all_projectile.remove(self)

    def move(self) : 
        if self.target == 0:
            self.rect.x += self.speed
        if self.target == 1:
            self.rect.x -= self.speed

        if self.target == 0:
            #verif si collision monstre
            for enemy in self.player.game.check_collision(self, self.player.game.all_enemy):
                if enemy.spawned == True or (enemy.rect.x < 1900 and enemy.type == 0):
                    self.remove()
                    enemy.damage(self.player.attack)

                #verif si collision projectile
                for proj in self.player.game.check_collision(self, enemy.all_projectile):
                    self.remove()
                    proj.remove()

            #verifier si le projectile n'est plus présent sur l'ecran
            if self.rect.x > 1920:
                self.remove()

        elif self.target == 1:
            #verif si collision joueur
            if self.player.game.check_collision(self, self.player.game.all_players):
                self.remove()
                #Mettre les damages ici
                self.player.damage(self.damage)

            #verif si collision projectile
            for proj in self.player.game.check_collision(self, self.player.all_projectile):
                self.remove()
                proj.remove()

            #verifier si le projectile n'est plus présent sur l'ecran
            if self.rect.x < -200:
                self.remove()