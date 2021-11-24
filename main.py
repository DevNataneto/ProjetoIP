import pygame,sys
from pygame.time import Clock

#elementos_da_tela
tela_altura = 600
tela_largura = 1200
tela = pygame.display.set_mode((tela_largura,tela_altura))
fps = pygame.time.Clock()
pygame.display.set_caption('Space Invaders')

#inicio_jogo
pygame.init
#jogo_rodando
while True:
    #pega_eventos_do_jogo
    for evento in pygame.event.get():
    #Quit_game  
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #elementos_da_tela
    tela.fill(pygame.Color('lightblue'))


    #atualiza_tela
    pygame.display.update()
    fps =  60
    
pygame.quit()
