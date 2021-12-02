import pygame,sys
from pygame.time import Clock
from inimigos import *
from nave import *
pygame.font.init()

def desenha_fundo():
    ponto_txt = fonte.render(f'Pontos: {pontos}', 1, (255,255,255))
    tela.blit(fundo, (0, 0))
    tela.blit(vidas, (tela_largura - 130, tela_altura - 45))
    tela.blit(ponto_txt, (20, tela_altura - 45))

def desenha():
    jogador_nave()
    desenha_aliens()
    
clock = pygame.time.Clock()
fps = 60
alien_v = 1
fonte = pygame.font.SysFont("bahnschrift",30)
pontos = 0
#cria tiros
tiro_lista = []
tirorect_lista = []
cooldown = 500
ultimo_tiro = 0

#inicia jogo
pygame.init
#MENU AQUI :)
while True:
    agora = pygame.time.get_ticks()
    aperta = pygame.key.get_pressed()   
    clock.tick(fps)
    desenha_fundo()
    #analisa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()            
            sys.exit()
    #move as naves
    for i in range (32):
        rects_lista[i].x += alien_v
    if rects_lista[7].right >= tela_largura:
        alien_v *= -1
        for i in range (32):
            rects_lista[i].move_ip(0,+5)
    if rects_lista[0].left <= 0:
        alien_v *= -1
        for i in range (32):
            rects_lista[i].move_ip(0,+5)
    #atira
    if aperta[pygame.K_SPACE] and agora - ultimo_tiro > 700:
        png_tiro = pygame.image.load("imagens\Teste.png")
        tirojogador = pygame.transform.scale(png_tiro, (10, 20)) 
        tirorect = tirojogador.get_rect()
        tiro_lista.append(tirojogador)
        tirorect_lista.append(tirorect)
        tirorect.center = jogador_rect.centerx, jogador_rect.top + 5
        ultimo_tiro = agora
    for i in range(len(tirorect_lista)):
        tela.blit(tirojogador, tirorect_lista[i])
        tirorect_lista[i].y -=8

    desenha()
    jogador_movimento()
    pygame.display.flip()

pygame.quit()
