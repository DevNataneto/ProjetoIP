from typing import Counter
import pygame
from pygame import mixer

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
contador = 0
level = 5
alien_v = level

#timer do jogo
fonte_timer = pygame.font.SysFont("Consantia",60)
timer = 4
ultimo_timer = pygame.time.get_ticks()

#sons do jogo
mixer.init()
pygame.mixer.init(44100, -16, 2, 512)
explosao_som = pygame.mixer.Sound("sons\explosao1.wav")
explosao_som.set_volume(0.25)
explosao2_som = pygame.mixer.Sound("sons\explosao2.wav")
explosao2_som.set_volume(0.50)
tiro_som = pygame.mixer.Sound("sons\Tiro.wav")
tiro_som.set_volume(0.25)
menu_selecao = pygame.mixer.Sound("sons/menu_selecao.wav")
menu_selecao.set_volume(0.25)
selec_menu = pygame.mixer.Sound("sons/selec_menu.wav")
selec_menu.set_volume(0.25)
musica_tema = pygame.mixer.music.load("sons/tema.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.10)
