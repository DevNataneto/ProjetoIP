import pygame
from elementos_base import *
from nave import *
import random

linhas = 5
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
        alien_rect.center = (85 + coluna * 90, linha * 70 + 50)

#desenha os aliens nos seus respectivos rects
def desenha_aliens():
    for i in range (len(alienrect_lista)):
        tela.blit(aliens_lista[i], alienrect_lista[i])

#cria tiro do alien
png_tiroalien = pygame.image.load("imagens\Teste.png")
tiroalien = pygame.transform.scale(png_tirojogador, (6, 12)) 
tiroalien_lista = []
tiroalienrect_lista = []
cooldown_alien = 1000
ultimo_tiroalien = 0

        