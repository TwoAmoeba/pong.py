import pygame

# Inicialización
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variables de los jugadores
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15
player1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Velocidades
player_speed = 6
ball_speed_x = 4
ball_speed_y = 4

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controles de los jugadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += player_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += player_speed

    # Movimiento
