import pygame,sys
from pygame.time import Clock

#codigos_jogador
class Jogador(pygame.sprite.Sprite):
    #cria_jogador
    def __init__(self, x , y, vida):
        pygame.sprite.Sprite.__init__(self)
        self.image_small = pygame.image.load("imagens\jogador_nave.png")
        self.image = pygame.transform.scale(self.image_small, (65,65))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vida = vida
        self.dano = vida

    #atualiza_tudo
    def atualiza(self):
        velocidade = 1
        aperta = pygame.key.get_pressed()
        #movimentos_jogador
        if aperta[pygame.K_RIGHT]:
            self.rect.x += velocidade
        if aperta[pygame.K_LEFT]:
            self.rect.x -= velocidade
        if aperta[pygame.K_UP]:
            self.rect.y -= velocidade
        if aperta[pygame.K_DOWN]:
            self.rect.y += velocidade

        #limita_jogador    
        if self.rect.top <= 0:
           self.rect.top = 0
        if self.rect.bottom >= (tela_altura - 30):
            self.rect.bottom = (tela_altura - 30)
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= tela_largura:
            self.rect.right = tela_largura

        #vida_jogador
        pygame.draw.rect(tela, vermelho, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.dano > 0:
            pygame.draw.rect(tela, verde, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.dano / self.vida)), 15))

#elementos_base_da_tela
tela_largura = 1200
tela_altura = 700
tela = pygame.display.set_mode((tela_largura,tela_altura))
fps = pygame.time.Clock()
pygame.display.set_caption('Space Invaders')
fundo_small = pygame.image.load("imagens\espaço.png")
fundo = pygame.transform.scale(fundo_small, (tela_largura,tela_altura))
#cores
vermelho = (255,0,0)
verde = (0,255,0)

#todos_sprites
grupo_jogador= pygame.sprite.Group()

#elementos_add_da_tela
jogador = Jogador(int(tela_largura / 2), tela_altura - 100, 3)
grupo_jogador.add(jogador)


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
    jogador.atualiza()
    
    #elementos_na_tela
    grupo_jogador.draw(tela)

    #atualiza_tela
    pygame.display.update()
    
pygame.quit()
