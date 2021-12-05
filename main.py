import pygame,sys
from pygame.time import Clock
from inimigos import *
from nave import *
import random


def desenha_fundo():
    ponto_txt = fonte.render(f'Pontos: {pontos}', 1, (255,255,255))
    tela.blit(fundo, (0, 0))
    tela.blit(vidas, (tela_largura - 130, tela_altura - 45))
    tela.blit(ponto_txt, (20, tela_altura - 45))

def desenha():
    jogador_nave()
    desenha_aliens()

def game_over():
    pass

#inicia jogo
pygame.init
#MENU AQUI :)
while True:
    jogador_mask = pygame.mask.from_surface(jogador)
    contador += 1
    agora = pygame.time.get_ticks()
    aperta = pygame.key.get_pressed()   
    clock.tick(fps)
    desenha_fundo()
    
    #tira vidas
    if vida == 2:
        png_vidas = pygame.image.load("imagens\coracoes_2.png")
    if vida == 1:
        png_vidas = pygame.image.load("imagens\coracoes_1.png")
    if vida == 0:
        png_vidas = pygame.image.load("imagens\coracoes_0.png")
    vidas = pygame.transform.scale(png_vidas, (140,35))
    
    #mexe os aliens
    for i in range (len(alienrect_lista)):
        alienrect_lista[i].x += alien_v
    if contador > 55 :
        alien_v *= -1
        contador *= -1
        for i in range (len(alienrect_lista)): 
            alienrect_lista[i].move_ip(0,+5)
    #alien atira
    if agora - ultimo_tiroalien > cooldown_alien and len(tiroalienrect_lista) < 8 and len(alienrect_lista) > 0:
        tiroalienrect = tiroalien.get_rect()
        tiroalienrect_lista.append(tiroalienrect)
        alien_atacante = random.choice (alienrect_lista)
        tiroalienrect.center = alien_atacante.centerx, alien_atacante.bottom
        ultimo_tiroalien = agora
    #move o tiro
    for i in tiroalienrect_lista:
        tela.blit(tiroalien, i)
        i.y +=4
        #exclui o tiro
        if i.top >= tela_altura or i.colliderect(jogador_rect):
            tiroalienrect_lista.remove(i)
        if i.colliderect(jogador_rect):
            vida -= 1

    
    #jogador atira
    if aperta[pygame.K_SPACE] and agora - ultimo_tirojogador > cooldown_jogador:
        tirorect = tirojogador.get_rect()
        tirorect_lista.append(tirorect)
        tirorect.center = jogador_rect.centerx, jogador_rect.top
        ultimo_tirojogador = agora
    #move o tiro
    for i in tirorect_lista:
        tela.blit(tirojogador, i)
        i.y -=8
        #exclui o tiro
        for j in alienrect_lista:
            if i.colliderect(j):
                alienrect_lista.remove(j)
                tirorect_lista.remove(i)
                pontos += 20
                break

    desenha()
    jogador_movimento()
    pygame.display.flip()
    
    #fecha o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()            
            sys.exit()

pygame.quit()
