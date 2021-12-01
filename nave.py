import pygame
from elementos_base import *


#cria tiros
png_tiro = pygame.image.load("imagens\Teste.png")
tiro_jogador = pygame.transform.scale(png_tiro, (15, 26)) 
tiro_rect = tiro_jogador.get_rect()

#cria vidinhas
vida = 3
png_vidas = pygame.image.load("imagens\coracoes_3.png")
vidas = pygame.transform.scale(png_vidas, (140,35))

#posiciona jogador
jogador_rect.center = tela_largura / 2, tela_altura - 70
jogador_lista = [jogador_rect]
tiro_lista = []

def jogador_nave():
    for i in jogador_lista:
        tela.blit(jogador,i)

def jogador_tiro():
    for i in tiro_lista:
        tela.blit(tiro_jogador,i)

def jogador_movimento():
    tiro_rect.y -=4
    aperta = pygame.key.get_pressed()
    if aperta[pygame.K_LEFT]:
        jogador_rect.move_ip(-2, 0)
    if aperta[pygame.K_RIGHT]:
        jogador_rect.move_ip(2, 0)
    if aperta[pygame.K_UP]:
        jogador_rect.move_ip(0, -2)
    if aperta[pygame.K_SPACE]:
        tiro_lista.append(tiro_rect)
        tiro_rect.center = jogador_rect.centerx, jogador_rect.top + 5
    if jogador_rect.left <= 0:
        jogador_rect.left = 0
    if jogador_rect.right >= tela_largura:
        jogador_rect.right = tela_largura
        