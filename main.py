import pygame
from pygame.locals import *

if __name__ == '__main__':
    pygame.init()
    
    surface = pygame.display.set_mode((1000, 500))
    surface.fill((53, 94, 59))
    pygame.display.flip()    
    
    running = True
while running == True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            pass
        elif event.type == QUIT:
            running = False
 