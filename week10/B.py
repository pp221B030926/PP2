import pygame
import datetime
from math import pi, sin, cos

size = 800
center = (size / 2, size / 2)
clock_radius = 400
fps = 60
current_time = datetime.datetime.now

pygame.init()
screen = pygame.display.set_mode([size, size])
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()

def numbers(number, number_size, position):
    font = pygame.font.SysFont('Arial', number_size, bold = True)
    text = font.render(number, True, pygame.Color('white'))
    text_rect = text.get_rect(center = (position))
    screen.blit(text, text_rect)


def polar_to_cartesian(r, theta):
    x,y = r * sin(pi * theta / 180), r * cos(pi * theta / 180)
    return x + size / 2, -(y - size / 2)


while True:
    screen.fill(pygame.Color('black'))

    pygame.draw.circle(screen, pygame.Color('white'), center, clock_radius - 10, 5)
    pygame.draw.circle(screen, pygame.Color('white'), center, 10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    
    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute
    hour = current_time.hour


    for num in range(1, 13):
        numbers(str(num), 80, polar_to_cartesian(clock_radius - 80, num * 30))
    pygame.display.flip()
    clock.tick(fps)