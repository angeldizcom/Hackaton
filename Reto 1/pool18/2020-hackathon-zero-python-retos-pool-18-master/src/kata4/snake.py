import pygame, sys, time, random
from pygame.locals import *

#pygame.init()
#play_surface = pygame.display.set_mode((500, 500))
#fps = pygame.time.Clock()

class Snake():
    position = [100,50]
    body = [[100,50], [90,50],[80,50]]
    direction = "RIGHT"
    change = direction

    # Manejo del pressed [KEYDOWN] de las teclas [K_RIGHT - K_LEFT - K_UP -K_DOWN ]
    def controller(self, event, pygame):
        
    # Controla el cambio de  las direcciones
    # Orientaciones
    # Vertical      -> Movimientos [RIGHT - LEFT]
    # Horizontal    -> Movimientos [UP - DOWN]
    # Incremento del movimiento 
    if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_UP:
		    self.direction = "UP" 
		if event.key == pygame.K_DOWN:
			self.direction = "DOWN" 
        if event.key == pygame.K_LEFT:
		    self.direction = "LEFT" 
        if event.key == pygame.K_RIGHT:
		    self.direction = "RIGHT" 

    def changeDirection(self):
        #
        if self.change == "RIGHT":
            self.position[0] = self.position[0] + 1
            self.position[0] = self.position[0] + 1
            self.body.insert(0, list(self.position))    
        elif self.change == "LEFT":
            self.position[0] = self.position[0] - 1
            self.body.insert(0, list(self.position))
        elif self.change == "UP":
            self.position[1] = self.position[1] + 1
            self.body.insert(0, list(self.position))
        else: 
            self.position[1] = self.position[1] - 1
            self.body.insert(0, list(self.position))
        #

class Game():
    run = True
    food_pos = 0
    score = 0

    def __init__(self):
        self.food_spawn()

    # función de salida
    def exit(self, event, pygame):
        #
        pygame.quit()
        self.exit()
    
    # Posición aleatorio entre el ranto [0,49] * 10  
    def food_spawn(self):
        food_pos_x = 10 * random.choice((0,49))
        food_pos_y = 10 * random.choice((0,49))
        self.food_pos = [food_pos_x,food_pos_y]

    # Si colisionas con una fruta, sumas 1
    # Sino decrementas en 1 el body del snake
    def eat(self, snake):
        #
        if((snake.position[0] == self.food_pos[0]) and (snake.position[1] == self.food_pos[1])):
            snake.body
        #  

    # Mensajes de salida cuando el snake muere
    # Posición snake[0] >= 500 ó snake[0] <= 0                  -> Muere
    # Posición snake[1] >= 500 ó snake[1] <= 0                  -> Muere
    # Posición del snake choca con sigo mismo menos la cabeza   -> Muere 
    def dead(self, snake):
        #
        #
        #
        
        #
        #
        #
        
        #
        #
        #
        
            
# Entry Point
def main():
    # Descomentar para lanzar el juego en local
    # Comentar para validar con el oráculo
    # pygame.init()
    # play_surface = pygame.display.set_mode((500, 500))
    # fps = pygame.time.Clock()

    snake = Snake()
    game = Game()

    # Bucle principal
    while game.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
			    game.exit(event, pygame)
            else:
                snake.controller(event, pygame)
        
        snake.changeDirection()

        game.eat(snake)

        # Dibujar Snake
        play_surface.fill((0,0,0))
        for pos in snake.body:
            pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))

        game.dead(snake)

        pygame.display.flip()
        fps.tick(60)

        
# Comienza la aventura!!!!
# Descomentar para lanzar el juego en local
# Comentar para validar con el oráculo
# main()
# pygame.quit()
