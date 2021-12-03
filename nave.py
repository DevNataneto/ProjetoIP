import pygame
from elementos_base import *

#cria jogador
jogador_rect.center = tela_largura / 2, tela_altura - 70
jogador_lista = [jogador_rect]
#cria vidinhas
vida = 3
png_vidas = pygame.image.load("imagens\coracoes_3.png")
vidas = pygame.transform.scale(png_vidas, (140,35))

def jogador_nave():
    for i in jogador_lista:
        tela.blit(jogador,i)

#move o jogador
def jogador_movimento():
    
    aperta = pygame.key.get_pressed()
    if aperta[pygame.K_LEFT]:
        jogador_rect.x -=4
    if aperta[pygame.K_RIGHT]:
        jogador_rect.x +=4

    if jogador_rect.left <= 0:
        jogador_rect.left = 0
    if jogador_rect.right >= tela_largura:
        jogador_rect.right = tela_largura
        