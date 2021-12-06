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
    fimjogo = 0
    if len(alienrect_lista) == 0:
        fimjogo = 1
    if vida == 0:
        fimjogo = -1
    return fimjogo

#inicia jogo
pygame.init
while True:
    aperta = pygame.key.get_pressed()   
    clock.tick(fps)
    desenha_fundo()
    #timer
    if timer > 0:
        timer_txt = fonte_timer.render('Se prepare!', 1, (255,255,255))
        timer_numero = fonte_timer.render(f'{timer}', 1, (255,255,255))
        tela.blit(timer_txt, (tela_largura / 2 -  120, tela_altura / 2))
        tela.blit(timer_numero, (tela_largura / 2 -  10, tela_altura / 2 + 50))
        timer_tempo = pygame.time.get_ticks()
        if timer_tempo - ultimo_timer > 1000:
            timer -= 1
            ultimo_timer = timer_tempo

    if timer == 0 and game_over() == 0 and vida > 0:
        contador += 1
        agora = pygame.time.get_ticks()
        jogador_movimento()

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
            if i.top >= tela_altura:
                tiroalienrect_lista.remove(i)
            if i.colliderect(jogador_rect):
                vida -= 1
                explosao2_som.play()
                tiroalienrect_lista.remove(i)
                
        #jogador atira
        if aperta[pygame.K_SPACE] and agora - ultimo_tirojogador > cooldown_jogador:
            tirorect = tirojogador.get_rect()
            tirorect_lista.append(tirorect)
            tirorect.center = jogador_rect.centerx, jogador_rect.top
            ultimo_tirojogador = agora
            tiro_som.play()
        #move o tiro
        for i in tirorect_lista:
            tela.blit(tirojogador, i)
            i.y -=8
            #exclui o tiro
            for j in alienrect_lista:
                if i.colliderect(j):
                    explosao_som.play()
                    alienrect_lista.remove(j)
                    tirorect_lista.remove(i)
                    pontos += 20
                    break
    #tira vidas
    if vida == 2:
        png_vidas = pygame.image.load("imagens\coracoes_2.png")
    if vida == 1:
        png_vidas = pygame.image.load("imagens\coracoes_1.png")
    if vida == 0:
        png_vidas = pygame.image.load("imagens\coracoes_0.png")
    vidas = pygame.transform.scale(png_vidas, (140,35))

    desenha()
    game_over()
    if game_over() == 1:
        ganhou_txt = fonte_timer.render('Você ganhou!', 1, (255,255,255))
        tela.blit(ganhou_txt, (tela_largura / 2 -  140, tela_altura / 2 - 20))
    if game_over() == -1:
        perdeu_txt = fonte_timer.render('Você perdeu!', 1, (255,255,255))
        tela.blit(perdeu_txt, (tela_largura / 2 -  140, tela_altura / 2 + 50))

    pygame.display.flip()
    #fecha o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()            
            sys.exit()
pygame.quit()
