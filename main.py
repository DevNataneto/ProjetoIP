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

#variaveis do jogo
clock = pygame.time.Clock()
fps = 60
fonte = pygame.font.SysFont("bahnschrift",30)
pontos = 0
alien_v = 1
contador = 0

#cria tiro do jogador
png_tirojogador = pygame.image.load("imagens\Teste.png")
tirojogador = pygame.transform.scale(png_tirojogador, (10, 20)) 
tiro_lista = []
tirorect_lista = []
cooldown_jogador = 500
ultimo_tirojogador = 0

#cria tiro do alien
png_tiroalien = pygame.image.load("imagens\Teste.png")
tiroalien = pygame.transform.scale(png_tirojogador, (6, 12)) 
tiroalien_lista = []
tiroalienrect_lista = []
cooldown_alien = 1000
ultimo_tiroalien = 0

#inicia jogo
pygame.init
#MENU AQUI :)
while True:
    contador += 1
    agora = pygame.time.get_ticks()
    aperta = pygame.key.get_pressed()   
    clock.tick(fps)
    desenha_fundo()
    #analisa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()            
            sys.exit()

    #mexe os aliens
    for i in range (len(alienrect_lista)):
        alienrect_lista[i].x += alien_v
    if contador > 68:
        alien_v *= -1
        contador *= -1
        for i in range (len(alienrect_lista)): 
            alienrect_lista[i].move_ip(0,+5)
    #alien atira
    if agora - ultimo_tiroalien > cooldown_alien and len(tiroalienrect_lista) < 6 and len(alienrect_lista) > 0:
        tiroalienrect = tiroalien.get_rect()
        tiroalienrect_lista.append(tiroalienrect)
        tiroalienrect.center = alien_rect.centerx, alien_rect.bottom
        ultimo_tiroalien = agora
    #move o tiro
    for i in tiroalienrect_lista:
        tela.blit(tiroalien, i)
        i.y +=4
        #exclui o tiro
        if i.top >= tela_altura:
            tiroalienrect_lista.remove(i) 


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
        if i.bottom <= 0 :
            tirorect_lista.remove(i)
                  
        for j in alienrect_lista:
            if j.colliderect(i):
                alienrect_lista.remove(j)
                #tirorect_lista.remove(i)

    desenha()
    jogador_movimento()
    pygame.display.flip()

pygame.quit()
