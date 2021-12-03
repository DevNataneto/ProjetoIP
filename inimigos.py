import pygame
from elementos_base import *
from nave import *
import random

linhas = 4
colunas = 8
aliens_lista = []
alienrect_lista = []

#cria e posiciona os aliens
for linha in range(linhas):
    for coluna in range(colunas):
        png_alien = pygame.image.load("imagens\Inimigo" + str(random.randint(1,4)) + ".png")
        alien = pygame.transform.scale(png_alien, (60,65))
        alien_rect = alien.get_rect()
        aliens_lista.append(alien)
        alienrect_lista.append(alien_rect)
        alien_rect.center = (100 + coluna * 100, linha * 75 + 50)

#desenha os aliens nos seus respectivos rects
def desenha_aliens():
    for i in range (len(alienrect_lista)):
        tela.blit(aliens_lista[i], alienrect_lista[i])
        