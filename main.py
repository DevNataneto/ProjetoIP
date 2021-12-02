import pygame,sys
from pygame.time import Clock
from inimigos import *
from nave import *

def desenha_fundo():
    tela.blit(fundo, (0, 0))
    tela.blit(vidas, (10, tela_altura - 40))

def desenha():
    jogador_nave()
    jogador_tiro()
    desenha_aliens()

fps = 60
clock = pygame.time.Clock()
alien_v = 1
#inicia jogo
pygame.init
while True:
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
    
    desenha()
    jogador_movimento()

    pygame.display.flip()

pygame.quit()
