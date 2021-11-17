import pygame,sys,random,time

def movimento_jogador1():
    jogador1.y += jogador_v

    if jogador1.top <= 0:
        jogador1.top = 0
    if jogador1.bottom >= tela_altura:
        jogador1.bottom = tela_altura

def movimento_jogador2():
    if jogador2.top < bola.y:
        jogador2.top += jogador2_v
    if jogador2.bottom > bola.y:
        jogador2.bottom -= jogador2_v
    if jogador2.top <= 0:
        jogador2.top = 0
    if jogador2.bottom >= tela_altura:
        jogador2.bottom = tela_altura

ponto_1 = 0
ponto_2 = 0
def movimento_bola():
    global bola_v_x,bola_v_y,ponto_1,ponto_2,jogador1,jogador2
    bola.x += bola_v_x
    bola.y += bola_v_y

    if bola.bottom >= tela_altura or bola.top <= 0:
        bola_v_y = bola_v_y * -1
    if bola.right >= tela_largura:
        ponto_2 += +1
        reset_bola()
        jogador1.center = (tela_largura - 5, tela_altura / 2)
        jogador2.center = (5, tela_altura / 2)
    if bola.left <= 0:
        ponto_1 += +1
        jogador1.center = (tela_largura - 5, tela_altura / 2)
        jogador2.center = (5, tela_altura / 2)
        reset_bola()
    if bola.colliderect(jogador1) or bola.colliderect(jogador2):
        bola_v_x = bola_v_x * -1

def reset_bola():
    global bola_v_y,bola_v_x
    bola.center = (tela_largura/2,tela_altura/2)
    bola_v_y *= random.choice((1,-1))
    bola_v_x *= random.choice((1,-1))

#Cores
verde_fav = (100,255,100)
azul_fav = (0,180,240)
preto = (0,0,0)
#Inicia_jogo
pygame.init()
#Cria a tela e seus elementos
clock = pygame.time.Clock()
tela_largura = 1200
tela_altura = 600
tela = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Pong')


#figuras
bola = pygame.Rect(tela_largura/2-10,tela_altura/2-10,20,20)
jogador1 = pygame.Rect(tela_largura-10,tela_altura/2-70,10,140)
jogador2 = pygame.Rect(0,tela_altura/2-70,10,140)
linha = pygame.Rect(tela_largura/2,0,10,10)
jogo_font = pygame.font.Font("freesansbold.ttf",20)
time_font = pygame.font.Font("freesansbold.ttf",20)
#velocidade
bola_v_x = 6.5 * random.choice((1,-1))
bola_v_y = 6.5 * random.choice((1,-1))
jogador_v = 0
jogador2_v = 5

#Loop_jogo
while True:
    for evento in pygame.event.get():
        #Para sair do jogo
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Movimentacao do jogador
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                jogador_v += 5
            if evento.key == pygame.K_UP:
                jogador_v -= 5
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_DOWN:
                jogador_v -= 5
            if evento.key == pygame.K_UP:
                jogador_v += 5
    #Movimentacao_rect
    movimento_bola()
    movimento_jogador1()
    movimento_jogador2()
    #Exibindo a tela e suas coisas
    tela.fill(pygame.Color('lightblue'))
    pygame.draw.aaline(tela,preto,(tela_largura/2,0),(tela_largura/2,tela_altura))
    pygame.draw.rect(tela,pygame.Color('red'),jogador1)
    pygame.draw.rect(tela,pygame.Color('red'),jogador2)
    pygame.draw.ellipse(tela,pygame.Color('red'),bola)

    jogador_text = jogo_font.render(f"{ponto_1}",True,preto)
    inimigo_text = jogo_font.render(f"{ponto_2}",True,preto)
    tela.blit(jogador_text,(tela_largura/2 + 15,tela_altura/2 + 10))
    tela.blit(inimigo_text, (tela_largura / 2 - 25, tela_altura / 2 + 10))

    pygame.display.update()
    clock.tick(60)
    #fim_jogo
    if ponto_1 == 10:
        print('voce ganhou!')
        break
    if ponto_2 == 10:
        print('o oponente ganhou!')
        break

pygame.quit()
