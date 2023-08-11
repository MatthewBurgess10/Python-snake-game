import pygame
from pygame.locals import *
import time
import random


class apple:
    def __init__(self, surface):
        self.parent_screen = surface
        apple = pygame.image.load('pythonsnakegameapple.png')
        self.s_apple = pygame.transform.scale(apple, (50, 50))
        
        self.b_x = random.randint(0, surface.get_width()-50)
        self.b_y = random.randint(0, surface.get_height()-50)
    def apple_draw(self):
        self.parent_screen.blit(self.s_apple, (self.b_x, self.b_y))
        pygame.display.flip()

SIZE = 40
class snake:
    def __init__(self, surface, length):
        self.length = length
        self.parent_screen = surface
        block = pygame.image.load('snakeblock.png')
        self.smallerblock = pygame.transform.scale(block, (50, 50))
        self.block_x = [SIZE]*length
        self.block_y = [SIZE]*length
        self.direction = 'down'
           
    def draw(self):
        self.parent_screen.fill((53, 94, 59))
        for i in range(self.length):
            self.parent_screen.blit(self.smallerblock, (self.block_x[i], self.block_y[i]))
        pygame.display.flip()
    def move_up(self):
        self.block_y +=10
        self.draw()
    def move_down(self):
        self.block_y -=10
        self.draw()
    def move_left(self):
        self.block_x -=10
        self.draw()
    def move_right(self):
        self.block_x +=10
        self.draw()
    
    def walk(self):
    
        for i in range(self.length-1,0,-1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]
        
        if self.direction == 'up':
            self.block_y[0] -= SIZE
        elif self.direction == 'down':
            self.block_y[0] += SIZE
        elif self.direction == 'left':
            self.block_x[0] -= SIZE
        elif self.direction == 'right':
            self.block_x[0] += SIZE
        self.draw()
    
  


class Game:
    def __init__(self):    #this is the game initialization function
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 1000))
        self.snake = snake(self.surface, 6)     #Number 6 is how many times the snake image is printed on the surface
        self.snake.draw()
        self.apple = apple(self.surface)
    def run(self):
        running = True

        while running == True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.direction = 'up'
                    if event.key == K_DOWN:
                        self.snake.direction = 'down'
                    if event.key == K_LEFT:
                        self.snake.direction = 'left'
                    if event.key == K_RIGHT:
                        self.snake.direction = 'right'
                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            self.apple.apple_draw()
            time.sleep(0.3)
   

if __name__ == '__main__':
    game = Game()
    game.run()
    
    
    
    
    pygame.display.flip() 
  
 