import pygame
from pygame.locals import * 

if __name__ == "__main__":
    pygame.init()
    
    surface = pygame.display.set_mode((500, 500))
    surface.fill((255,255,255))
    pygame.display.flip()
    
    
run = True

while run == True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            pass
        elif event.ype == QUIT:
            run = False
    
    
    
#video finished at 11.30 
 
    
    