# Traci Trojan

class Ship:

    def __init__(self, game, vector=Vector()):
        self.game = game
        self.screen = game.screen
        self.velocity = vector

        self.screen_rect = game.screen.get_rect()
        self.image = pg.image.load('ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.lasers = pg.sprite.Group()

    def fire(self):
        laser = Laser(game=self.game)
        self.lasers.add(laser)

    def remove_lasers(self): self.lasers.remove()

    def move(self):
        if self.velocity == Vector():
            return
        self.rect.left += self.velocity.x
        self.rect.top += self.velocity.y
        self.game.limit_on_screen(self.rect)

    def draw(self): self.screen.blit(self.image, self.rect)

    def update(self):
        fleet = self.game.fleet
        self.move()
        self.draw()
        for laser in self.lasers.sprites():
            laser.update()
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0:
                self.lasers.remove(laser)
        pg.sprite.groupcollide(self.lasers, fleet.aliens, True, True)

        if not fleet.aliens:
            self.game.restart()
