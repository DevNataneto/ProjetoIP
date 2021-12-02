import pygame

#elementos base da tela
tela_largura = 900
tela_altura = 700
tela = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Space Invaders')
png_fundo = pygame.image.load("imagens\espaço.png")
fundo = pygame.transform.scale(png_fundo, (tela_largura,tela_altura))

#cria jogador
png_jogador = pygame.image.load("imagens\jogador_nave.png")
jogador = pygame.transform.scale(png_jogador, (60,65))
jogador_rect = jogador.get_rect()

#cria placar
