import pygame

#elementos base da tela
tela_largura = 800
tela_altura = 750
tela = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Space Invaders')
png_fundo = pygame.image.load("imagens\espaço.png")
fundo = pygame.transform.scale(png_fundo, (tela_largura,tela_altura))

#variaveis do jogo
clock = pygame.time.Clock()
fps = 60
pygame.font.init()
fonte = pygame.font.SysFont("bahnschrift",30)
pontos = 0
alien_v = 1
contador = 0
