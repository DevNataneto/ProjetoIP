import pygame,sys
from pygame.time import Clock

#codigos_jogador
class Jogador(pygame.sprite.Sprite):
    #cria_jogador
    def __init__(self, x , y):
        pygame.sprite.Sprite.__init__(self)
        self.image_small = pygame.image.load("imagens\jogador_nave.png")
        self.image = pygame.transform.scale(self.image_small, (65,65))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    #atualiza_tudo
    def movimento(self):
        velocidade = 1
        aperta = pygame.key.get_pressed()
        #movimentos_jogador
        if aperta[pygame.K_RIGHT]:
            self.rect.x += velocidade
        if aperta[pygame.K_LEFT]:
            self.rect.x -= velocidade
        #limita_jogador    
        if self.rect.left <= 30:
            self.rect.left = 30
        if self.rect.right >= tela_largura - 30:
            self.rect.right = tela_largura - 30

#vida_jogador
class Vidinhas(pygame.sprite.Sprite):
    def __init__(self, x , y, vida):
        pygame.sprite.Sprite.__init__(self)
        if vida == 3:
            self.image_small = pygame.image.load("imagens\coracoes_3.png")
        if vida == 2:
            self.image_small = pygame.image.load("imagens\coracoes_2.png")
        if vida == 1:
            self.image_small = pygame.image.load("imagens\coracoes_1.png")
        if vida == 0:
            self.image_small = pygame.image.load("imagens\coracoes_0.png")
        self.image = pygame.transform.scale(self.image_small, (140,35))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def movimento(self):
        velocidade = 1
        aperta = pygame.key.get_pressed()
        #movimentos_vidas
        if aperta[pygame.K_RIGHT]:
            self.rect.x += velocidade
        if aperta[pygame.K_LEFT]:
            self.rect.x -= velocidade
        #limita_vida  
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= tela_largura + 15:
            self.rect.right = tela_largura + 15

class Tiros(pygame.sprite.Sprite):
    #cria_tiros
    def __init__(self, x , y):
        pygame.sprite.Sprite.__init__(self)
        self.image_small = pygame.image.load("imagens\coracoes_0.png")
        self.image = pygame.transform.scale(self.image_small, (65,65))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

#elementos_base_da_tela
tela_largura = 1200
tela_altura = 700
tela = pygame.display.set_mode((tela_largura,tela_altura))
fps = pygame.time.Clock()
pygame.display.set_caption('Space Invaders')
fundo_small = pygame.image.load("imagens\espaço.png")
fundo = pygame.transform.scale(fundo_small, (tela_largura,tela_altura))

#todos_sprites
grupo_jogador= pygame.sprite.Group()

#elementos_add_da_tela
jogador = Jogador(int(tela_largura / 2), tela_altura - 80)
vidas = Vidinhas(int(tela_largura / 2 + 6), tela_altura - 30, 3)
grupo_jogador.add(jogador)
grupo_jogador.add(vidas)


#inicio_jogo
pygame.init
#jogo_rodando
while True:
    fps =  60
    #analisa_eventos
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT:
            pygame.quit()            
            sys.exit()
    tela.blit(fundo, (0,0))
    #atualiza_jogador
    jogador.movimento()
    vidas.movimento()
    #elementos_na_tela
    grupo_jogador.draw(tela)

    #atualiza_tela
    pygame.display.update()
    
pygame.quit()
