import pygame,sys
from pygame.time import Clock

#elementos_base_da_tela
tela_largura = 1200
tela_altura = 700
tela = pygame.display.set_mode((tela_largura,tela_altura))
fps = pygame.time.Clock()
pygame.display.set_caption('Space Invaders')

#elementos_add_da_tela
fundo = pygame.image.load("imagens\espaço.png")
fundo_ok = pygame.transform.scale(fundo, (tela_largura,tela_altura))


#inicio_jogo
pygame.init
#jogo_rodando
while True:
    #analisa_eventos
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT:
            pygame.quit()            
            sys.exit()


    #elementos_na_tela
    tela.fill(pygame.Color('lightblue'))
    tela.blit(fundo_ok, (0,0))


    #atualiza_tela
    pygame.display.update()
    fps =  60
    
pygame.quit()
