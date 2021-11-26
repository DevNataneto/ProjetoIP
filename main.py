import pygame,sys
from pygame.time import Clock


#elementos_base_da_tela
fps = pygame.time.Clock()
tela_largura = 1200
tela_altura = 700
tela = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Space Invaders')
png_fundo = pygame.image.load("imagens\espaço.png")
fundo = pygame.transform.scale(png_fundo, (tela_largura,tela_altura))
x = (tela_largura / 2 - 35)
y = (tela_altura - 105) 
velocidade_jogador = 1
velocidade_bala = 0.5

#cria_inimigos


#cria_tiro
png_tiro = pygame.image.load("imagens\Teste.png")
tiro_jogador = pygame.transform.scale(png_tiro, (15, 26)) 

#cria_jogador
png_jogador = pygame.image.load("imagens\jogador_nave.png")
jogador = pygame.transform.scale(png_jogador, (60,65))

#cria_vidinhas
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

#desenha_na_tela


def desenha_tudo():
    tela.blit(fundo, (0, 0))
    tela.blit(jogador, (x, tela_altura - 100))
    tela.blit(vidas, (10, tela_altura - 40))
    
#inicio_jogo
pygame.init

while True:
    fps = 30
    segura = pygame.key.get_pressed()
    #analisa_eventos
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT:
            pygame.quit()            
            sys.exit()

    #desenha_elementos
    desenha_tudo()
    
    #ações_gerais
    if segura[pygame.K_RIGHT] and x < tela_largura - 70 :
        x += velocidade_jogador
    if segura[pygame.K_LEFT] and x > 5:
        x -= velocidade_jogador

    #!FALTA ARRUMAR O TIRO!    
    if segura[pygame.K_SPACE]:
        tela.blit(tiro_jogador, (x + 25, y))
        y -= velocidade_bala


    pygame.display.update()
    
pygame.quit()
