import pygame,sys
from pygame.time import Clock

#desenha_na_tela
def desenha():
    tela.blit(fundo, (0, 0))
    tela.blit(jogador, (x - 2, tela_altura - 100))
    tela.blit(vidas, (x - 35, tela_altura - 40))
    
#elementos_base_da_tela
fps = pygame.time.Clock()
tela_largura = 1200
tela_altura = 700
tela = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Space Invaders')
png_fundo = pygame.image.load("imagens\espaço.png")
fundo = pygame.transform.scale(png_fundo, (tela_largura,tela_altura))
x = tela_largura / 2 - 35
y = 0
velocidade = 1

#jogador
png_jogador = pygame.image.load("imagens\jogador_nave.png")
jogador = pygame.transform.scale(png_jogador, (65,65))
#vidinhas
vida = 3
if vida == 3:
    png_vidas = pygame.image.load("imagens\coracoes_3.png")
if vida == 2:
    png_vidas = pygame.image.load("imagens\coracoes_2.png")
if vida == 1:
    png_vidas = pygame.image.load("imagens\coracoes_1.png")
if vida == 0:
    png_vidas = pygame.image.load("imagens\coracoes_0.png")
vidas = pygame.transform.scale(png_vidas, (140,35))

#inicio_jogo
pygame.init

while True:
    fps =  30
    #analisa_eventos
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT:
            pygame.quit()            
            sys.exit()
    aperta = pygame.key.get_pressed()
    
    #ações_gerais
    if aperta[pygame.K_RIGHT] and x < tela_largura - 90 :
        x += velocidade
    if aperta[pygame.K_LEFT] and x > 30:
        x -= velocidade
    
    
    #desenha_elementos
    desenha()
    
    pygame.display.update()
    
pygame.quit()
