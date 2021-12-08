import pygame
from elementos_base import *

#cria jogador
png_jogador = pygame.image.load("imagens\jogador_nave.png")
jogador = pygame.transform.scale(png_jogador, (60,65))
jogador_rect = jogador.get_rect()
jogador_rect.center = tela_largura / 2, tela_altura - 70
jogador_lista =[jogador]
jogadorrect_lista = [jogador_rect]

#cria tiro do jogador
png_tirojogador = pygame.image.load("imagens\Teste.png")
tirojogador = pygame.transform.scale(png_tirojogador, (8, 16))
tiro_lista = []
tirorect_lista = []
cooldown_jogador = 500
ultimo_tirojogador = 0

#cria vidinhas
vida = 3
png_vidas = pygame.image.load("imagens\coracoes_3.png")
vidas = pygame.transform.scale(png_vidas, (140,35))

def desenha_nave():
    if len(jogadorrect_lista) > 0:
        for i in jogador_lista:
            tela.blit(i, jogador_rect)

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
