import pygame 
from random import randrange
pygame.init()
size = (800,800)
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
color = ('pink')
color1 = ('green')
color2 = ('white')
snow = pygame.image.load('1.png')
clock = pygame.time.Clock()
done = False 
block = 50
x = 100
y = 675
snow1 = snow.get_size()
x1 = randrange(0, 750)
y1 = randrange(0, 500, 50)
rect = pygame.Rect(0, 700, 800, 100)
font_end = pygame.font.SysFont('Arial', 66, bold = True)
a = 0
while not done: 
    screen.fill('cyan')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 100
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 20    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 20
    if x > 800:
        x = 0
    if x < 0:
        x = 800
    if y > 800:
        y = 0
    if y < 0:
        y = 800
    screen.blit(snow,(x1,y1))
    if y1 <= 695 and a == 0:
        y1 += 5
        print(x1, y1)      
        print(x,y)
    if y1 == 645:
        a = 1
    if y1 >= 0 and a == 1:
        y1 -= 5
    if y1 == 0:
        a = 0
    if x + snow1[0] >= x1 and x <= x1 + snow1[0] and y <= y1 and y + snow1[1]>= y1:
        render_end = font_end.render('GAME OVER',True, pygame.Color('red'))
        screen.blit(render_end, (190, 300))
        done = True
    pygame.draw.circle(screen, color,(x,y) ,25)
    pygame.draw.rect(screen, color1, rect)
    clock.tick(60)
    if y < 675:
        y += 5
    pygame.display.flip()
pygame.quit()