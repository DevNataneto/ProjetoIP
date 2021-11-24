import pygame 

#codigos_jogador:
class Jogador(pygame.sprite.Sprite):
    def __init__(self, x , y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img\jogador.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    