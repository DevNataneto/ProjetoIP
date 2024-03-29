import pygame,sys
from pygame.constants import MOUSEBUTTONDOWN
from pygame.time import Clock
from inimigos import *
from nave import *
import random
from pygame import mixer

def desenha_fundo():
    ponto_txt = fonte.render(f'Pontos: {pontos}', 1, (255,255,255))
    tela.blit(fundo, (0, 0))
    tela.blit(vidas, (tela_largura - 130, tela_altura - 45))
    tela.blit(ponto_txt, (20, tela_altura - 45))

def desenha():
    desenha_nave()
    desenha_aliens()

def game_over():
    fimjogo = 0
    if len(alienrect_lista) == 0:
        fimjogo += 1
    if vida == 0:
        fimjogo = -1
    return fimjogo

#Variáveis do Menu
menu = True
click = False
i = 0
som1 = True
som2 = True
som3 = True
som4 = True
som5 = True

#titulo do menu
titulo_1 = pygame.image.load("imagens/titulo_1.png")
titulo1_tamanho = pygame.transform.scale(titulo_1, (400,400))
titulo1_rect = titulo1_tamanho.get_rect()
titulo1_rect.center = (tela_largura/2, tela_altura/3)

#background do menu
bg_menu = pygame.image.load("imagens/testebg.png")
bg_menu_tamanho = pygame.transform.scale(bg_menu, (tela_largura, tela_altura))

#botão de start game
botao_1 = pygame.image.load("imagens/botao_start1.png")
botao_1_select = pygame.image.load("imagens/botao_start2.png")
botao1_tamanho = pygame.transform.scale(botao_1, (100,100))
botao1_rect = botao1_tamanho.get_rect()
botao1_rect.center = (tela_largura/2, tela_altura/1.5)

#botão de sair do jogo
botao_2 = pygame.image.load("imagens/botao_sair1.png")
botao_2_select = pygame.image.load("imagens/botao_sair2.png")
botao2_tamanho = pygame.transform.scale(botao_2, (100,100))
botao2_rect = botao2_tamanho.get_rect()
botao2_rect.center = (tela_largura/2, tela_altura/1.2)

#inicia jogo
pygame.init()
while True:
    if menu == True:
        #rolagem do background do menu
        tela.blit(bg_menu_tamanho, (i,0))   
        tela.blit(bg_menu_tamanho, (tela_largura+i, 0))
        if i == -tela_largura:
            tela.blit(bg_menu_tamanho, (tela_largura+i, 0))
            i = 0
        i -= 1
        tela.blit(titulo1_tamanho, titulo1_rect)
        tela.blit(botao1_tamanho, botao1_rect)
        tela.blit(botao2_tamanho, botao2_rect)
        mx, my = pygame.mouse.get_pos()
        #muda o sprite do botão de sair
        if botao2_rect.collidepoint((mx, my)):
            botao2_tamanho = pygame.transform.scale(botao_2_select, (100,100))
            if som1 == True:
                menu_selecao.play()
                som1 = False
        else:
            botao2_tamanho = pygame.transform.scale(botao_2, (100,100))
            som1 = True
        #muda o sprite do botão de start
        if botao1_rect.collidepoint((mx, my)):
            botao1_tamanho = pygame.transform.scale(botao_1_select, (100,100))
            if som2 == True:
                menu_selecao.play()
                som2 = False 
        else:
            botao1_tamanho = pygame.transform.scale(botao_1, (100,100))
            som2 = True
        #leva para o jogo ao clicar em jogar
        if botao1_rect.collidepoint((mx, my)):
            if click:
                menu = False

        #sai do jogo ao clicar que sair
        if botao2_rect.collidepoint((mx, my)):
            if click:
                pygame.quit()            
                sys.exit()
        pygame.display.flip()
        clock.tick(fps)
        click = False
        #fecha o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()            
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
    else:
        pygame.mixer.music.stop()
        aperta = pygame.key.get_pressed()   
        clock.tick(fps)
        desenha_fundo()
        
        #timer
        if timer > 0:
            timer_txt = fonte.render('Prepare-se!', 1, (255,255,255))
            timer_numero = fonte.render(f'{timer}', 1, (255,255,255))
            tela.blit(timer_txt, (tela_largura / 2 -  115, tela_altura - 240))
            tela.blit(timer_numero, (tela_largura / 2 -  12, tela_altura - 190))
            timer_tempo = pygame.time.get_ticks()
            if timer_tempo - ultimo_timer > 1000:
                timer -= 1
                ultimo_timer = timer_tempo
            if timer == 3 and som3 == True:
                selec_menu.play()
                som3 = False
            if timer == 2 and som4 == True:
                selec_menu.play()
                som4 = False
            if timer == 1 and som5 == True:
                selec_menu.play()
                som5 = False
        #inicio do jogo
        if timer == 0 and game_over() == 0 and vida > 0:
            contador += 1
            agora = pygame.time.get_ticks()
            jogador_movimento()

        #mexe os aliens
            for i in range (len(alienrect_lista)):
                alienrect_lista[i].x += alien_v
            if contador > 55:
                alien_v *= -1
                contador *= -1
                for i in range (len(alienrect_lista)): 
                    alienrect_lista[i].move_ip(0,+5)
            #alien atira
            if agora - ultimo_tiroalien > cooldown_alien and len(tiroalienrect_lista) < 7 + level and len(alienrect_lista) > 0:
                tiroalienrect = tiroalien.get_rect()
                tiroalienrect_lista.append(tiroalienrect)
                alien_atacante = random.choice (alienrect_lista)
                tiroalienrect.center = alien_atacante.centerx, alien_atacante.bottom
                ultimo_tiroalien = agora
            #move o tiro
            for i in tiroalienrect_lista:
                tela.blit(tiroalien, i)
                i.y += 1 + level 
                #exclui o tiro
                if i.top >= tela_altura:
                    tiroalienrect_lista.remove(i)
                if i.colliderect(jogador_rect):
                    vida -= 1
                    explosao2_som.play()
                    tiroalienrect_lista.remove(i)
                    #jogador fica branco quando toma dano
                    png_jogadordano = pygame.image.load("imagens\jogador_nave_dano.png")
                    jogadordano = pygame.transform.scale(png_jogadordano, (60, 65))
                    jogador_lista[0] = jogadordano
                    conta = 0
            conta += 1
            if conta > 6:
                jogador_lista[0] =jogador

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
                for j in range (len(alienrect_lista)):
                    if i.colliderect(alienrect_lista[j]):
                        explosao_som.play()
                        alienrect_lista.pop(j)
                        aliens_lista.pop(j)
                        tirorect_lista.remove(i)
                        pontos += 20
                        break

        #muda as vidas
        if vida == 2:
            png_vidas = pygame.image.load("imagens\coracoes_2.png")
        if vida == 1:
            png_vidas = pygame.image.load("imagens\coracoes_1.png")
        if vida == 0:
            png_vidas = pygame.image.load("imagens\coracoes_0.png")
        vidas = pygame.transform.scale(png_vidas, (140,35))

        desenha()
        game_over()
        if game_over() == 1 and level == 7:
            ganhou_txt = fonte_win.render('Parabéns você ganhou!', 1, (255,255,255))
            ganhou_txt2 = fonte_win.render(f'Sua pontuação total foi de {pontos} pontos', 1, (255,255,255))
            tela.blit(ganhou_txt, (150, tela_altura / 2 ))
            tela.blit(ganhou_txt2, (10, tela_altura / 2 + 50 ))   
        if game_over() == 1 and level != 7:
            ganhou_txt = fonte2.render('Você Sobreviveu!', 1, (255,255,255))
            ganhou_txt2 = fonte2.render('Aperte enter para continuar', 1, (255,255,255))
            tela.blit(ganhou_txt, (260, tela_altura / 2 ))
            tela.blit(ganhou_txt2, (220, tela_altura / 2 + 50 ))
        if game_over() == -1:
            perdeu_txt = fonte2.render('Você perdeu, aperte enter para tentar novamente', 1, (255,255,255))
            tela.blit(perdeu_txt, (80, tela_altura - 140))
            jogador_lista.clear()
            
        #Reinicia o level
        if aperta[pygame.K_RETURN] and vida == 0:
            aliens_lista.clear()
            alienrect_lista.clear()
            contador = 0
            conta = 0
            pontos = 0
            vida = 3
            if vida == 3:
                png_vidas = pygame.image.load("imagens\coracoes_3.png")
            vidas = pygame.transform.scale(png_vidas, (140,35))
            tiro_lista.clear()
            tirorect_lista.clear()
            cooldown_jogador = 500
            ultimo_tirojogador = 0
            jogador_lista.append(jogador)
            jogador_rect.center = tela_largura / 2, tela_altura - 70
            linhas = level
            colunas = 8
            aliens_lista.clear()
            alienrect_lista.clear()
            tiroalien_lista.clear()
            tiroalienrect_lista.clear()
            for linha in range(linhas):
                for coluna in range(colunas):
                    png_alien = pygame.image.load("imagens\Inimigo" + str(random.randint(1,4)) + ".png")
                    alien = pygame.transform.scale(png_alien, (60,65))
                    alien_rect = alien.get_rect()
                    aliens_lista.append(alien)
                    alienrect_lista.append(alien_rect)
                    alien_rect.center = (85 + coluna * 90, linha * 70 + 60)

        #Passa de fase
        if aperta[pygame.K_RETURN] and len(alienrect_lista) == 0 and level < 7:
            level += 1
            contador = 0
            conta = 0
            vida = 3
            if vida == 3:
                png_vidas = pygame.image.load("imagens\coracoes_3.png")
            vidas = pygame.transform.scale(png_vidas, (140,35))
            tiro_lista = []
            tirorect_lista = []
            cooldown_jogador = 500
            ultimo_tirojogador = 0
            jogador_rect.center = tela_largura / 2, tela_altura - 70
            linhas = level
            colunas = 8
            aliens_lista = []
            alienrect_lista = []
            tiroalien_lista = []
            tiroalienrect_lista = []
            for linha in range(linhas):
                for coluna in range(colunas):
                    png_alien = pygame.image.load("imagens\Inimigo" + str(random.randint(1,4)) + ".png")
                    alien = pygame.transform.scale(png_alien, (60,65))
                    alien_rect = alien.get_rect()
                    aliens_lista.append(alien)
                    alienrect_lista.append(alien_rect)
                    alien_rect.center = (85 + coluna * 90, linha * 70 + 60)


            #desenha os aliens nos seus respectivos rects
            def desenha_aliens():
                for i in range (len(alienrect_lista)):
                    tela.blit(aliens_lista[i], alienrect_lista[i])
        pygame.display.flip()
        #fecha o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()            
                sys.exit()
pygame.quit()
