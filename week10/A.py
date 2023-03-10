import pygame 
from random import randrange

size = 800 
block = 50 
score = 0
x, y = randrange(0, size, block), randrange(0, size, block)

apple = randrange(0, size, block), randrange(0,size, block)
length = 1 
snake = [{x,y}]
dx, dy = 0, 0
fps = 10
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
pygame.init()
screen = pygame.display.set_mode([size, size])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold = True)
font_end = pygame.font.SysFont('Arial', 66, bold = True)
img = pygame.image.load('game.jpg').convert()

while True:
    screen.blit(img, (0,0))

    screen.fill(pygame.Color('black'))
    #draw snake, apple 
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, block - 1, block - 1))
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, block, block))
    
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    screen.blit(render_score, (670, 5))
    #snake movement
    x += dx * block
    y += dy * block
    snake.append((x,y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0, size, block), randrange(0, size, block)
        length += 1
        fps += 0.5
        score += 1
    if x < 0 or x > size or y < 0 or y > size or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME_OVER',True, pygame.Color('orange'))
            screen.blit(render_end, (190, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(fps)

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0 
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0    
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
