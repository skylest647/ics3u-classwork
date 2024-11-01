import pygame
pygame.init()
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
white = (255,255,255)
black = (0,0,0)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
running = True
ghostx = 10
ghosty = 199
ghostSpeedx = 5
ghostSpeedy = 5
ghostx2 = 100
ghosty2 = 250
ghostSpeedx2 = 8
ghostSpeedy2 = 3
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    pygame.draw.rect(screen, (13, 71 , 1),(0,380,1000,100))
    pygame.draw.circle(screen, (white),(100, 70), 50 )
    #ghost
    pygame.draw.rect(screen, (white),(ghostx, ghosty,20,50))
    pygame.draw.circle(screen, (white),(ghostx + 10, ghosty + 2), 10 )
    pygame.draw.circle(screen, (black),(ghostx + 14, ghosty ), 3 )
    pygame.draw.circle(screen, (black),(ghostx + 5, ghosty ), 3 )
    #ghost2
    pygame.draw.rect(screen, (white),(ghostx2 - 10, ghosty2,40,70))
    pygame.draw.circle(screen, (white),(ghostx2 + 10, ghosty2 + 2), 20 )
    pygame.draw.circle(screen, (black),(ghostx2 + 19, ghosty2 ), 3 )
    pygame.draw.circle(screen, (black),(ghostx2 + 3, ghosty2 ), 3 )
    ghosty += ghostSpeedy
    ghostx += ghostSpeedx
    if ghostx >= 200 or ghostx <= 9:
        ghostSpeedx *= -1
    if ghosty >= 200 or ghosty <= 170:
        ghostSpeedy *= -1

    ghosty2 += ghostSpeedy2
    ghostx2 += ghostSpeedx2
    if ghostx2>= 200 or ghostx2 <= 9:
        ghostSpeedx2 *= -1
    if ghosty2 >= 300 or ghosty2 <= 150:
        ghostSpeedy2 *= -1
    pygame.draw.rect(screen, (87, 7 , 7),(300,150,300,250))
    pygame.draw.polygon(screen, (87, 7, 7), ((290,150),(610,150),(450,50)))
    pygame.draw.rect(screen, (50, 7 , 7),(430, 300,50,100))
    pygame.draw.circle(screen, (255,255,0),(470, 350 ), 3 )
    pygame.display.flip()
    clock.tick(30)