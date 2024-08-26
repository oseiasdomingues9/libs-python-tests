import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configura a tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pulo da Bola')

# Define cores
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Posição e velocidade da bola
ball_pos = [400, 500]
ball_radius = 20
ball_speed_x = 5
ball_speed_y = 0

# Configurações do pulo
gravity = 1  # Gravidade
jump_power = -15  # Força do pulo (negativo porque y cresce para baixo)
on_ground = True  # Verifica se a bola está no chão

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtém o estado das teclas
    keys = pygame.key.get_pressed()

    # Move a bola horizontalmente com as setas do teclado
    if keys[pygame.K_LEFT]:
        ball_pos[0] -= ball_speed_x
    if keys[pygame.K_RIGHT]:
        ball_pos[0] += ball_speed_x

    # Se a bola estiver no chão e a tecla de espaço for pressionada, pular
    if keys[pygame.K_SPACE] and on_ground:
        ball_speed_y = jump_power
        on_ground = False

    # Aplica a gravidade
    ball_speed_y += gravity
    ball_pos[1] += ball_speed_y

    # Verifica se a bola atingiu o chão
    if ball_pos[1] >= 600 - ball_radius:
        ball_pos[1] = 600 - ball_radius
        ball_speed_y = 0
        on_ground = True

    # Preenche a tela com preto
    screen.fill(BLACK)

    # Desenha a bola
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a velocidade do loop
    pygame.time.Clock().tick(60)
