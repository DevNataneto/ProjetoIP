import pygame
from elementos_base import *
from nave import *

#carrega_imagens
png_inimigo_verde = pygame.image.load("imagens\Inimigo1.png")
inimigo_verde = pygame.transform.scale(png_inimigo_verde, (60,65))
inimigo_verde1_rect = inimigo_verde.get_rect()
inimigo_verde2_rect = inimigo_verde.get_rect()
inimigo_verde3_rect = inimigo_verde.get_rect()
inimigo_verde4_rect = inimigo_verde.get_rect()
inimigo_verde5_rect = inimigo_verde.get_rect()
inimigo_verde6_rect = inimigo_verde.get_rect()
inimigo_verde7_rect = inimigo_verde.get_rect()
inimigo_verde8_rect = inimigo_verde.get_rect()

png_inimigo_azul = pygame.image.load("imagens\Inimigo2.png")
inimigo_azul = pygame.transform.scale(png_inimigo_azul, (60,65))
inimigo_azul1_rect = inimigo_azul.get_rect()
inimigo_azul2_rect = inimigo_azul.get_rect()
inimigo_azul3_rect = inimigo_azul.get_rect()
inimigo_azul4_rect = inimigo_azul.get_rect()
inimigo_azul5_rect = inimigo_azul.get_rect()
inimigo_azul6_rect = inimigo_azul.get_rect()
inimigo_azul7_rect = inimigo_azul.get_rect()
inimigo_azul8_rect = inimigo_azul.get_rect()

png_inimigo_vermelho = pygame.image.load("imagens\Inimigo3.png")
inimigo_vermelho = pygame.transform.scale(png_inimigo_vermelho, (60,65))
inimigo_vermelho1_rect = inimigo_vermelho.get_rect()
inimigo_vermelho2_rect = inimigo_vermelho.get_rect()
inimigo_vermelho3_rect = inimigo_vermelho.get_rect()
inimigo_vermelho4_rect = inimigo_vermelho.get_rect()
inimigo_vermelho5_rect = inimigo_vermelho.get_rect()
inimigo_vermelho6_rect = inimigo_vermelho.get_rect()
inimigo_vermelho7_rect = inimigo_vermelho.get_rect()
inimigo_vermelho8_rect = inimigo_vermelho.get_rect()

png_inimigo_amarelo = pygame.image.load("imagens\Inimigo4.png")
inimigo_amarelo = pygame.transform.scale(png_inimigo_amarelo, (60,65))
inimigo_amarelo1_rect = inimigo_amarelo.get_rect()
inimigo_amarelo2_rect = inimigo_amarelo.get_rect()
inimigo_amarelo3_rect = inimigo_amarelo.get_rect()
inimigo_amarelo4_rect = inimigo_amarelo.get_rect()
inimigo_amarelo5_rect = inimigo_amarelo.get_rect()
inimigo_amarelo6_rect = inimigo_amarelo.get_rect()
inimigo_amarelo7_rect = inimigo_amarelo.get_rect()
inimigo_amarelo8_rect = inimigo_amarelo.get_rect()

# movimenta inimigos
def movimento_inimigo1():
    if inimigo_verde8_rect.right <= tela_largura - 10:
        inimigo_verde1_rect.x += 1
        inimigo_verde2_rect.x += 1
        inimigo_verde3_rect.x += 1
        inimigo_verde4_rect.x += 1
        inimigo_verde5_rect.x += 1
        inimigo_verde6_rect.x += 1
        inimigo_verde7_rect.x += 1
        inimigo_verde8_rect.x += 1

def movimento_inimigo2():
    if inimigo_azul8_rect.right <= tela_largura - 10:
        inimigo_azul1_rect.move_ip(1,0)
        inimigo_azul2_rect.move_ip(1,0)
        inimigo_azul3_rect.move_ip(1,0)
        inimigo_azul4_rect.move_ip(1,0)
        inimigo_azul5_rect.move_ip(1,0)
        inimigo_azul6_rect.move_ip(1,0)
        inimigo_azul7_rect.move_ip(1,0)
        inimigo_azul8_rect.move_ip(1,0)

def movimento_inimigo3():
    if inimigo_vermelho8_rect.right <= tela_largura - 10:
        inimigo_vermelho1_rect.move_ip(1,0)
        inimigo_vermelho2_rect.move_ip(1,0)
        inimigo_vermelho3_rect.move_ip(1,0)
        inimigo_vermelho4_rect.move_ip(1,0)
        inimigo_vermelho5_rect.move_ip(1,0)
        inimigo_vermelho6_rect.move_ip(1,0)
        inimigo_vermelho7_rect.move_ip(1,0)
        inimigo_vermelho8_rect.move_ip(1,0)
        
def movimento_inimigo4():
    if inimigo_amarelo8_rect.right <= tela_largura - 10:
        inimigo_amarelo1_rect.move_ip(1,0)
        inimigo_amarelo2_rect.move_ip(1,0)
        inimigo_amarelo3_rect.move_ip(1,0)
        inimigo_amarelo4_rect.move_ip(1,0)
        inimigo_amarelo5_rect.move_ip(1,0)
        inimigo_amarelo6_rect.move_ip(1,0)
        inimigo_amarelo7_rect.move_ip(1,0)
        inimigo_amarelo8_rect.move_ip(1,0)



def morre_inimigo_verde():
    for i in inimigo_verde1:
        tela.blit(inimigo_verde,i)
    for i in inimigo_verde2:
        tela.blit(inimigo_verde,i)
    for i in inimigo_verde3:
        tela.blit(inimigo_verde,i)
    for i in inimigo_verde4:
        tela.blit(inimigo_verde,i)
    for i in inimigo_verde5:
        tela.blit(inimigo_verde,i)
    for i in inimigo_verde6:
        tela.blit(inimigo_verde,i)
    for i in inimigo_verde7:
        tela.blit(inimigo_verde,i)
    for i in inimigo_verde8:
        tela.blit(inimigo_verde,i)

def colisão_verde():
    if tiro_rect.colliderect(inimigo_verde1_rect):
        inimigo_verde1.clear()
    if tiro_rect.colliderect(inimigo_verde2_rect):
        inimigo_verde2.clear()
    if tiro_rect.colliderect(inimigo_verde3_rect):
        inimigo_verde3.clear()
    if tiro_rect.colliderect(inimigo_verde4_rect):
        inimigo_verde4.clear()
    if tiro_rect.colliderect(inimigo_verde5_rect):
        inimigo_verde5.clear()
    if tiro_rect.colliderect(inimigo_verde6_rect):
        inimigo_verde6.clear()
    if tiro_rect.colliderect(inimigo_verde7_rect):
        inimigo_verde7.clear()
    if tiro_rect.colliderect(inimigo_verde8_rect):
        inimigo_verde8.clear()
#desenha e mata inimigos

def morre_inimigo_azul():
    for i in inimigo_azul1:
        tela.blit(inimigo_azul,i)
    if tiro_rect.colliderect(inimigo_azul1_rect):
        inimigo_azul1.clear()
    for i in inimigo_azul2:
        tela.blit(inimigo_azul,i)
    if tiro_rect.colliderect(inimigo_azul2_rect):
        inimigo_azul2.clear()
    for i in inimigo_azul3:
        tela.blit(inimigo_azul,i)
    if tiro_rect.colliderect(inimigo_azul3_rect):
        inimigo_azul3.clear()
    for i in inimigo_azul4:
        tela.blit(inimigo_azul,i)
    if tiro_rect.colliderect(inimigo_azul4_rect):
        inimigo_azul4.clear()
    for i in inimigo_azul5:
        tela.blit(inimigo_azul,i)
    if tiro_rect.colliderect(inimigo_azul5_rect):
        inimigo_azul5.clear()
    for i in inimigo_azul6:
        tela.blit(inimigo_azul,i)
    if tiro_rect.colliderect(inimigo_azul6_rect):
        inimigo_azul6.clear()
    for i in inimigo_azul7:
        tela.blit(inimigo_azul,i)
    if tiro_rect.colliderect(inimigo_azul7_rect):
        inimigo_azul7.clear()
    for i in inimigo_azul8:
        tela.blit(inimigo_azul,i)
    if tiro_rect.colliderect(inimigo_azul8_rect):
        inimigo_azul8.clear()

def morre_inimigo_vermelho():
    for i in inimigo_vermelho1:
        tela.blit(inimigo_vermelho,i)
    if tiro_rect.colliderect(inimigo_vermelho1_rect):
        inimigo_vermelho1.clear()
    for i in inimigo_vermelho2:
        tela.blit(inimigo_vermelho,i)
    if tiro_rect.colliderect(inimigo_vermelho2_rect):
        inimigo_vermelho2.clear()
    for i in inimigo_vermelho3:
        tela.blit(inimigo_vermelho,i)
    if tiro_rect.colliderect(inimigo_vermelho3_rect):
        inimigo_vermelho3.clear()
    for i in inimigo_vermelho4:
        tela.blit(inimigo_vermelho,i)
    if tiro_rect.colliderect(inimigo_vermelho4_rect):
        inimigo_vermelho4.clear()
    for i in inimigo_vermelho5:
        tela.blit(inimigo_vermelho,i)
    if tiro_rect.colliderect(inimigo_vermelho5_rect):
        inimigo_vermelho5.clear()
    for i in inimigo_vermelho6:
        tela.blit(inimigo_vermelho,i)
    if tiro_rect.colliderect(inimigo_vermelho6_rect):
        inimigo_vermelho6.clear()
    for i in inimigo_vermelho7:
        tela.blit(inimigo_vermelho,i)
    if tiro_rect.colliderect(inimigo_vermelho7_rect):
        inimigo_vermelho7.clear()
    for i in inimigo_vermelho8:
        tela.blit(inimigo_vermelho,i)
    if tiro_rect.colliderect(inimigo_vermelho8_rect):
        inimigo_vermelho8.clear()

def morre_inimigo_amarelo():
    for i in inimigo_amarelo1:
        tela.blit(inimigo_amarelo,i)
    if tiro_rect.colliderect(inimigo_amarelo1_rect):
        inimigo_amarelo1.clear()
    for i in inimigo_amarelo2:
        tela.blit(inimigo_amarelo,i)
    if tiro_rect.colliderect(inimigo_amarelo2_rect):
        inimigo_amarelo2.clear()
    for i in inimigo_amarelo3:
        tela.blit(inimigo_amarelo,i)
    if tiro_rect.colliderect(inimigo_amarelo3_rect):
        inimigo_amarelo3.clear()
    for i in inimigo_amarelo4:
        tela.blit(inimigo_amarelo,i)
    if tiro_rect.colliderect(inimigo_amarelo4_rect):
        inimigo_amarelo4.clear()
    for i in inimigo_amarelo5:
        tela.blit(inimigo_amarelo,i)
    if tiro_rect.colliderect(inimigo_amarelo5_rect):
        inimigo_amarelo5.clear()
    for i in inimigo_amarelo6:
        tela.blit(inimigo_amarelo,i)
    if tiro_rect.colliderect(inimigo_amarelo6_rect):
        inimigo_amarelo6.clear()
    for i in inimigo_amarelo7:
        tela.blit(inimigo_amarelo,i)
    if tiro_rect.colliderect(inimigo_amarelo7_rect):
        inimigo_amarelo7.clear()
    for i in inimigo_amarelo8:
        tela.blit(inimigo_amarelo,i)
    if tiro_rect.colliderect(inimigo_amarelo8_rect):
        inimigo_amarelo8.clear()

inimigo_verde1=[inimigo_verde1_rect]
inimigo_verde2=[inimigo_verde2_rect]
inimigo_verde3=[inimigo_verde3_rect]
inimigo_verde4=[inimigo_verde4_rect]
inimigo_verde5=[inimigo_verde5_rect]
inimigo_verde6=[inimigo_verde6_rect]
inimigo_verde7=[inimigo_verde7_rect]
inimigo_verde8=[inimigo_verde8_rect]

inimigo_azul1=[inimigo_azul1_rect]
inimigo_azul2=[inimigo_azul2_rect]
inimigo_azul3=[inimigo_azul3_rect]
inimigo_azul4=[inimigo_azul4_rect]
inimigo_azul5=[inimigo_azul5_rect]
inimigo_azul6=[inimigo_azul6_rect]
inimigo_azul7=[inimigo_azul7_rect]
inimigo_azul8=[inimigo_azul8_rect]

inimigo_vermelho1=[inimigo_vermelho1_rect]
inimigo_vermelho2=[inimigo_vermelho2_rect]
inimigo_vermelho3=[inimigo_vermelho3_rect]
inimigo_vermelho4=[inimigo_vermelho4_rect]
inimigo_vermelho5=[inimigo_vermelho5_rect]
inimigo_vermelho6=[inimigo_vermelho6_rect]
inimigo_vermelho7=[inimigo_vermelho7_rect]
inimigo_vermelho8=[inimigo_vermelho8_rect]

inimigo_amarelo1=[inimigo_amarelo1_rect]
inimigo_amarelo2=[inimigo_amarelo2_rect]
inimigo_amarelo3=[inimigo_amarelo3_rect]
inimigo_amarelo4=[inimigo_amarelo4_rect]
inimigo_amarelo5=[inimigo_amarelo5_rect]
inimigo_amarelo6=[inimigo_amarelo6_rect]
inimigo_amarelo7=[inimigo_amarelo7_rect]
inimigo_amarelo8=[inimigo_amarelo8_rect]

#posiciona inimigos
inimigo_verde1_rect.center = tela_largura -850 , tela_altura -430
inimigo_verde2_rect.center = tela_largura -750 , tela_altura -430
inimigo_verde3_rect.center = tela_largura -650 , tela_altura -430
inimigo_verde4_rect.center = tela_largura -550 , tela_altura -430
inimigo_verde5_rect.center = tela_largura -450 , tela_altura -430
inimigo_verde6_rect.center = tela_largura -350 , tela_altura -430
inimigo_verde7_rect.center = tela_largura -250 , tela_altura -430
inimigo_verde8_rect.center = tela_largura -150 , tela_altura -430

inimigo_azul1_rect.center = tela_largura -850 , tela_altura -510
inimigo_azul2_rect.center = tela_largura -750 , tela_altura -510
inimigo_azul3_rect.center = tela_largura -650 , tela_altura -510
inimigo_azul4_rect.center = tela_largura -550 , tela_altura -510
inimigo_azul5_rect.center = tela_largura -450 , tela_altura -510
inimigo_azul6_rect.center = tela_largura -350 , tela_altura -510
inimigo_azul7_rect.center = tela_largura -250 , tela_altura -510
inimigo_azul8_rect.center = tela_largura -150 , tela_altura -510

inimigo_vermelho1_rect.center = tela_largura -850 , tela_altura -580
inimigo_vermelho2_rect.center = tela_largura -750 , tela_altura -580
inimigo_vermelho3_rect.center = tela_largura -650 , tela_altura -580
inimigo_vermelho4_rect.center = tela_largura -550 , tela_altura -580
inimigo_vermelho5_rect.center = tela_largura -450 , tela_altura -580
inimigo_vermelho6_rect.center = tela_largura -350 , tela_altura -580
inimigo_vermelho7_rect.center = tela_largura -250 , tela_altura -580
inimigo_vermelho8_rect.center = tela_largura -150 , tela_altura -580

inimigo_amarelo1_rect.center = tela_largura -850 , tela_altura -650
inimigo_amarelo2_rect.center = tela_largura -750 , tela_altura -650
inimigo_amarelo3_rect.center = tela_largura -650 , tela_altura -650
inimigo_amarelo4_rect.center = tela_largura -550 , tela_altura -650
inimigo_amarelo5_rect.center = tela_largura -450 , tela_altura -650
inimigo_amarelo6_rect.center = tela_largura -350 , tela_altura -650
inimigo_amarelo7_rect.center = tela_largura -250 , tela_altura -650
inimigo_amarelo8_rect.center = tela_largura -150 , tela_altura -650
