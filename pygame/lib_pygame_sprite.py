import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configura a tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sprite com Pulo')

# Define cores
BLACK = (0, 0, 0)

# Carrega a imagem do sprite
sprite_image = pygame.image.load('character.png')  # Use uma imagem PNG de um personagem
sprite_image = pygame.transform.scale(sprite_image, (50, 50))  # Redimensiona se necessário

# Define a classe Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)
        self.speed_x = 5
        self.speed_y = 0
        self.gravity = 1
        self.jump_power = -15
        self.on_ground = True

    def update(self):
        keys = pygame.key.get_pressed()
        
        # Movimento horizontal
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed_x
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed_x
        
        # Pulo
        if keys[pygame.K_SPACE] and self.on_ground:
            self.speed_y = self.jump_power
            self.on_ground = False
        
        # Aplica a gravidade
        self.speed_y += self.gravity
        self.rect.y += self.speed_y

        # Verifica se está no chão
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.speed_y = 0
            self.on_ground = True

# Cria um grupo de sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza os sprites
    all_sprites.update()

    # Preenche a tela com preto
    screen.fill(BLACK)

    # Desenha todos os sprites
    all_sprites.draw(screen)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a velocidade do loop
    pygame.time.Clock().tick(60)
