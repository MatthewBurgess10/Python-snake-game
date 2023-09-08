import pygame
from pygame.locals import *
import random
import pygame.time

class apple:
    def __init__(self, surface):
        self.parent_screen = surface
        apple = pygame.image.load('pythonsnakegameapple.png')
        self.s_apple = pygame.transform.scale(apple, (50, 50))
        
        self.b_x = random.randint(0, 20)*45
        self.b_y = random.randint(0, 20)*45
    def apple_draw(self):
        self.parent_screen.blit(self.s_apple, (self.b_x, self.b_y))
        pygame.display.flip()
    def apple_move(self):
        self.b_x = random.randint(0, 20)*45
        self.b_y = random.randint(0, 20)*45

SIZE = 40
class snake:
    def __init__(self, surface, length):
        self.length = length
        self.parent_screen = surface
        block = pygame.image.load('snakeblock.png')
        self.smallerblock = pygame.transform.scale(block, (45, 45))
        self.block_x = [SIZE]*length
        self.block_y = [SIZE]*length
        self.direction = 'down'
           #initializes an empty set

    def draw(self):
        self.parent_screen.fill((53, 94, 59))
        for i in range(self.length):
            self.parent_screen.blit(self.smallerblock, (self.block_x[i], self.block_y[i]))
        pygame.display.flip()
    def inc_length(self):
        self.length+=1
        self.block_x.append(-1)
        self.block_y.append(-1)
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
    
        
        
        if self.direction == 'up':
            self.block_y[0] -= SIZE
        if self.direction == 'down':
            self.block_y[0] += SIZE
        if self.direction == 'left':
            self.block_x[0] -= SIZE
        if self.direction == 'right':
            self.block_x[0] += SIZE
        for i in range(self.length-1,0,-1):
            self.block_x[i] = self.block_x[i - 1]
            self.block_y[i] = self.block_y[i - 1]
        self.draw()
        
        
class Game:
    def __init__(self):    #this is the game initialization function
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((1000, 1000))
        self.snake = snake(self.surface, 2)     #Number is how many times the snake image is printed on the surface
        self.snake.draw()
        self.apple = apple(self.surface)
        self.apple.apple_draw()
        self.clock = pygame.time.Clock()
        self.game_over = False

    def display_score(self):
        font = pygame.font.SysFont('arial', 25, bold=False, italic=False)
        score = font.render(f"score: {self.snake.length-1}", True, (250, 250, 250))
        self.surface.blit(score,(900, 10))
        
    def play(self):
        
        self.snake.walk()
        self.display_score()
        self.apple.apple_draw()
        
        #check for collisions with the apple
        if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.apple.b_x, self.apple.b_y):
            self.apple.apple_move()
            self.snake.inc_length()
        # Check for collisions with itself   
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.block_x[0], self.snake.block_y[0], self.snake.block_x[i], self.snake.block_x[i]):
                raise "game over"   
        # Check for collisions with walls 
        if (
            self.snake.block_x[0] < 0
            or self.snake.block_x[0] >= 1000
            or self.snake.block_y[0] < 0
            or self.snake.block_y[0] >= 1000                 
        ):
            print("hit a wall")
            self.game_over = True
        
    def is_collision(self, x1, y1, x2, y2):
        x1_min, x1_max = x1, x1 + SIZE
        y1_min, y1_max = y1, y1 + SIZE
        x2_min, x2_max = x2, x2 + SIZE
        y2_min, y2_max = y2, y2 + SIZE
        
        if x1_max > x2_min and x1_min < x2_max:
            if y1_max > y2_min and y1_min < y2_max:
                return True
        return False
    
    def gameover(self):
        font = pygame.font.SysFont('arial', 70, bold=False, italic=False)
        game_over_text = font.render('Game Over', True, (250, 0, 0))            
        self.surface.blit(game_over_text, (300, 300))
        pygame.display.flip()
        pygame.time.wait(2000)                 
        self.running = False
   
    def run(self):
        self.running = True
        pause = False
        while self.running == True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                    if not pause:
                        
                        if event.key == K_UP:
                            self.snake.direction = 'up'
                        if event.key == K_DOWN:
                            self.snake.direction = 'down'
                        if event.key == K_LEFT:
                            self.snake.direction = 'left'
                        if event.key == K_RIGHT:
                            self.snake.direction = 'right'
                    elif event.type == QUIT:
                    
                        self.running = False
             
                
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.gameover()
                pause = True
            
                

            
                
            #check for collisions with itself
            
            

                  
            
                
            
            
            if self.game_over == True:
                self.gameover()
                
            self.clock.tick(4)

if __name__ == '__main__':
    game = Game()
    game.run()
    
    
    
    
    pygame.display.flip() 
  
