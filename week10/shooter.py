import pygame
# variables
WIDTH,HEIGHT = 800, 640
FPS = 60
# moving
moving_left = False
moving_right = False
# init
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
BG = (144, 201, 120)

class Soldier(pygame.sprite.Sprite):

    def __init__(self,x,y,scale,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load('img/player/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def draw(self):
        screen.blit(self.image, self.rect)
    def move(self,moving_left,moving_right):
        dx, dy = 0, 0
        if moving_left:
            dx =- self.speed
        if moving_right:
            dx = self.speed
        self.rect.x += dx
        self.rect.y += dy
Player = Soldier(200, 200, 3,5)

while True:
    # draw
    screen.fill(BG)
    Player.draw()
    Player.move(moving_left, moving_right)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False    
    # display
    pygame.display.flip()
    clock.tick(FPS)