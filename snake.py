import sys
import pygame
import random
from pygame.locals import *

# Constantes
FPS = 10
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20
CELLS_HORIZONTAL = WINDOW_WIDTH // CELL_SIZE
CELLS_VERTICAL = WINDOW_HEIGHT // CELL_SIZE

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")

    snake = [{'x': CELLS_HORIZONTAL // 2, 'y': CELLS_VERTICAL // 2}]
    direction = 'right'
    apple = generate_apple(snake)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_w) and direction != 'down':
                    direction = 'up'
                elif event.key in (K_DOWN, K_s) and direction != 'up':
                    direction = 'down'
                elif event.key in (K_LEFT, K_a) and direction != 'right':
                    direction = 'left'
                elif event.key in (K_RIGHT, K_d) and direction != 'left':
                    direction = 'right'

        # Mover la serpiente
        move_snake(snake, direction)

        # Verificar si la serpiente ha comido la manzana
        if snake[0] == apple:
            apple = generate_apple(snake)
        else:
            del snake[-1]

        # Verificar si la serpiente chocó consigo misma o con los bordes
        if (snake[0]['x'] < 0 or snake[0]['x'] >= CELLS_HORIZONTAL or
            snake[0]['y'] < 0 or snake[0]['y'] >= CELLS_VERTICAL or
            snake[0] in snake[1:]):
            terminate()

        display.fill(BLACK)
        draw_snake(display, snake)
        draw_apple(display, apple)
        pygame.display.update()
        clock.tick(FPS)

def move_snake(snake, direction):
    if direction == 'up':
        new_head = {'x': snake[0]['x'], 'y': snake[0]['y'] - 1}
    elif direction == 'down':
        new_head = {'x': snake[0]['x'], 'y': snake[0]['y'] + 1}
    elif direction == 'left':
        new_head = {'x': snake[0]['x'] - 1, 'y': snake[0]['y']}
    elif direction == 'right':
        new_head = {'x': snake[0]['x'] + 1, 'y': snake[0]['y']}
    
    snake.insert(0, new_head)

def generate_apple(snake):
    while True:
        apple = {'x': random.randint(0, CELLS_HORIZONTAL - 1), 'y': random.randint(0, CELLS_VERTICAL - 1)}
        if apple not in snake:
            return apple
          
def draw_snake(display, snake):
    for segment in snake:
        pygame.draw.rect(display, GREEN, (segment['x'] * CELL_SIZE, segment['y'] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_apple(display, apple):
    pygame.draw.rect(display, RED, (apple['x'] * CELL_SIZE, apple['y'] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()