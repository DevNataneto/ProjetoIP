from os import remove
import pygame,sys
from pygame.time import Clock
from inimigos import *
from nave import *
 

def desenha():
    tela.blit(fundo, (0, 0))
    tela.blit(vidas, (10, tela_altura - 40))
    jogador_nave()
    jogador_tiro()
    morre_inimigo_verde()
    morre_inimigo_azul()
    morre_inimigo_vermelho()
    morre_inimigo_amarelo()
    
#inicia_jogo
pygame.init
while True:
    fps = 60
    desenha()
    #analisa_eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()            
            sys.exit()
    
    jogador_movimento()
    morre_inimigo_verde()
    morre_inimigo_azul()
    morre_inimigo_vermelho()
    morre_inimigo_amarelo()
    colisão_verde()
    pygame.display.flip()

pygame.quit()
