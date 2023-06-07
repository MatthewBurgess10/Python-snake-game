import pygame
from pygame.locals import * 
import sys

class snake:
    def __init__(self, main_screen):   #self allows u to access stuff in a defined class
        self.main_screen = main_screen
        self.large_block = pygame.image.load("snakeblock.png").convert()  #loads the image
        self.block = pygame.transform.scale(self.large_block, (50, 50)) #shrinks the image
        self.block_x = 100
        self.block_y = 100
    def draw(self, surface):
        surface.blit(self.block, (self.block_x, self.block_y))
class game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((12, 17, 17))
    
    def run(self):
        self.main_screen.blit(self.block, (self.block_x, self.block_y)) #draws the image at these coords
        
        
        
def draw_block(surface, self):
    surface.fill((12, 17, 17))
    surface.blit(self.block, (self.block_x, self.block_y))
    pygame.display.flip()
    

if __name__ == "__main__":
    Game = game()
    game.run()
    


    pygame.display.flip()  #makes changes visible to the user.
    
    
run = True

while run == True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
                
            if event.key == K_UP:
                block_y = block_y - 10
                draw_block()
            if event.key == K_DOWN:
                block_y = block_y + 10
                draw_block()
            if event.key == K_RIGHT:
                block_x = block_x + 10
                draw_block()
            if event.key == K_LEFT:
                block_x = block_x - 10 
                draw_block()
                
        elif event.type == QUIT:
            run = False
    
    
    
#video finished at 
 
    
    