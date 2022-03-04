import pygame
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("pong")

#variable that runs the game loop
doExit = False
p1x = 20
p1y = 200
p2x = 650
p2y = 200
bx = 350
by = 250
bVx = 5
bVy = 5
p1Score = 0
p2Score = 0
#clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

while not doExit: #game loop
   
   #event queue
    clock.tick(60) #set the fps
    
    for event in pygame.event.get(): #check if user did something
        if event.type == pygame.QUIT: #check if user clicked close
            doExit = True #flag that we are done so we exit gam loop
            
    
    #game loop goes here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
            p1y-=5
    if keys[pygame.K_s]:
        p1y+=5
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
            p2y-=5
    if keys[pygame.K_DOWN]:
        p2y+=5
    
    bx += bVx
    by += bVy
    
    #if bx < 0 or bx + 20 > 700:
       # bVx *= -1
        
    if by < 0 or by + 20 > 500:
        bVy *= -1
    #ball-paddle reflection
    if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
    if bx > p2x and by + 20 > p2y and by < p2y + 100:
        bVx *= -1
    if bx <= 0:
        bVx *= -1
        p2Score += 1
    if bx >= 700:
        bVx *= -1
        p1Score += 1
    #render section goes here
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (250,10))
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (420,10))

    #draw a line down the middle
    pygame.draw.line(screen, (255,255,255,), [349,0], [349, 500], 5)
    pygame.draw.rect(screen, (255, 255, 255), (p1x, p1y, 20, 100), 10)
    pygame.draw.rect(screen, (255, 255, 255), (p2x, p2y, 20, 100), 10)
    pygame.draw.circle(screen, (255, 255, 255), (bx, by), 10)

    #update the screen
    pygame.display.flip()
#end game loop
            
pygame.quit()#when game is done close pygame

