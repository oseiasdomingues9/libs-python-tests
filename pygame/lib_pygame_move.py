import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configura a tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Controle da Bola com as Setas do Teclado')

# Define cores
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Posição inicial da bola
#ball_pos = [horizontal, vertical]
ball_pos = [400, 300]
ball_radius = 20
ball_speed = 5

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtém o estado das teclas
    keys = pygame.key.get_pressed()

    # Move a bola com as setas do teclado
    if keys[pygame.K_LEFT]:
        ball_pos[0] = ball_pos[0] - ball_speed
    if keys[pygame.K_RIGHT]:
        ball_pos[0] += ball_speed
    if keys[pygame.K_UP]:
        ball_pos[1] -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_pos[1] += ball_speed
    if keys[pygame.K_SPACE]:
        ball_pos = [400, 300]    

    # Mantém a bola dentro dos limites da tela
    if ball_pos[0] < ball_radius:
        ball_pos[0] = ball_radius
    if ball_pos[0] > 800 - ball_radius:
        ball_pos[0] = 800 - ball_radius
    if ball_pos[1] < ball_radius:
        ball_pos[1] = ball_radius
    if ball_pos[1] > 600 - ball_radius:
        ball_pos[1] = 600 - ball_radius

    # Preenche a tela com preto
    screen.fill(BLACK)

    # Desenha a bola
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a velocidade do loop
    pygame.time.Clock().tick(60)
