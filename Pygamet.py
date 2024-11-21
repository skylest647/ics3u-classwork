import pygame
import pygame.draw_py
pygame.init()
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
white = (255,255,255)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

circle_x = 200
circle_y = 200
x = 5
y = 5
growx = 1
growy = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if x >= WIDTH  or x <= 0:
        growx *= -1
    x += growx
    if y >= HEIGHT or y <= 0:
        growy *= -1
    y += growy
    screen.fill(white)  
    pygame.draw.rect(screen, (50, 25 , 90), (y,x,x, y))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()