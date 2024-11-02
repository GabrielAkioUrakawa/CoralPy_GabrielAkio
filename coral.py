#!/usr/bin/python3
#
#   Copyright (c) 2023, Monaco F. J. <monaco@usp.br>
#   Copyright 2024 The Authors of Coral
#
#   This file is part of Coral.
#
#   Coral is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
import random
import sys
from enum import Enum

##
## Game customization.
##

WIDTH, HEIGHT = 800, 800     # Game screen dimensions.

HEAD_COLOR      = "#00aa00"  # Color of the snake's head.
DEAD_HEAD_COLOR = "#4b0082"  # Color of the dead snake's head.
TAIL_COLOR      = "#00ff00"  # Color of the snake's tail.
APPLE_COLOR     = "#aa0000"  # Color of the apple.
ARENA_COLOR     = "#202020"  # Color of the ground.
CONFIG_COLOR    = "#D3D3D3"  # Color of the config section.
GRID_COLOR      = "#3c3c3b"  # Color of the grid lines.
SCORE_COLOR     = "#ffffff"  # Color of the scoreboard.
LINE_COLOR     = "#000000"  # Color of lines in scoreboard.
MESSAGE_COLOR   = "#808080"  # Color of the game-over message.

WINDOW_TITLE    = "Coral"  # Window title.

velocity = [4, 7, 10,15]
size = [60, 40, 20]  
n_apple = [1, 2, 3] 
configs = [1, 1, 0]

##
## Game implementation.
##

pygame.init()

clock = pygame.time.Clock()

arena = pygame.display.set_mode((WIDTH, HEIGHT))

# BIG_FONT   = pygame.font.Font("assets/font/Ramasuri.ttf", int(WIDTH/8))
# SMALL_FONT = pygame.font.Font("assets/font/Ramasuri.ttf", int(WIDTH/20))

BIG_FONT   = pygame.font.Font("assets/font/GetVoIP-Grotesque.ttf", int(WIDTH/8))
SMALL_FONT = pygame.font.Font("assets/font/GetVoIP-Grotesque.ttf", int(WIDTH/20))

pygame.display.set_caption(WINDOW_TITLE)

game_on = 1

## This function is called when the snake dies.
def center_prompt(title, subtitle):

    # Show title and subtitle.

    center_title = BIG_FONT.render(title, True, MESSAGE_COLOR)
    center_title_rect = center_title.get_rect(center=(WIDTH/2, HEIGHT*(0.4)))
    arena.blit(center_title, center_title_rect)

    center_subtitle = SMALL_FONT.render(subtitle, True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*(0.6)))
    arena.blit(center_subtitle, center_subtitle_rect)
    
    center_subtitle = SMALL_FONT.render("Aperte C para configurar o jogo!", True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*(0.65)))
    arena.blit(center_subtitle, center_subtitle_rect)

    pygame.display.update()

   # Wait for a keypres or a game quit event.

    while ( event := pygame.event.wait() ):
        if event.type == pygame.KEYDOWN:
            break
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.key == pygame.K_q:          # 'Q' quits game
        pygame.quit()
        sys.exit()
    if event.key == pygame.K_c:
        config_prompt()
        
def draw_config(conf=[1,1,1]):
    velocity_string = ["Baixa", "Média", "Alta", "Extrema"]
    size_string = ["Pequeno", "Médio", "Grande"]
    f_string = ["Baixa", "Normal", "Alta"]
    arena.fill(CONFIG_COLOR)
    center_title = BIG_FONT.render("Configuração", True, MESSAGE_COLOR)
    center_title_rect = center_title.get_rect(center=(WIDTH/2, HEIGHT*(0.20)))
    arena.blit(center_title, center_title_rect)

    center_subtitle = SMALL_FONT.render("Utilize as setas para navegar!", True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*(0.30)))
    arena.blit(center_subtitle, center_subtitle_rect)
    center_subtitle = SMALL_FONT.render("Aperte J para jogar!", True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*(0.35)))
    arena.blit(center_subtitle, center_subtitle_rect)

    center_subtitle = SMALL_FONT.render("Velocidade:", True, LINE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*(0.45)))
    arena.blit(center_subtitle, center_subtitle_rect)
    center_subtitle = SMALL_FONT.render("{}".format(velocity_string[conf[0]]), True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*(0.50)))
    arena.blit(center_subtitle, center_subtitle_rect)
    
    center_subtitle = SMALL_FONT.render("Tamanho:", True, LINE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*(0.60)))
    arena.blit(center_subtitle, center_subtitle_rect)
    center_subtitle = SMALL_FONT.render("{}".format(size_string[conf[1]]), True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*(0.65)))
    arena.blit(center_subtitle, center_subtitle_rect)
    
    center_subtitle = SMALL_FONT.render("Frequência:", True, LINE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*(0.75)))
    arena.blit(center_subtitle, center_subtitle_rect)
    center_subtitle = SMALL_FONT.render("{}".format(f_string[conf[2]]), True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(center=(WIDTH/2, HEIGHT*(0.80)))
    arena.blit(center_subtitle, center_subtitle_rect)
    
    pygame.display.update()
    
def config_prompt():
    draw_config()

   # Wait for a keypres or a game quit event.
    n = 0
    stop = 0
    while True:
        if stop == 1:
            break
        for event in pygame.event.get():      
            if stop == 1:
                break     
        # App terminated
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:  
                    if n == 2:
                        n = 0  
                    else:
                        n += 1
                elif event.key == pygame.K_UP:   
                    if n == 0:
                        n = 2 
                    else:
                        n -= 1
                elif event.key == pygame.K_RIGHT: 
                    if configs[n] == 2:
                        configs[n] = 0
                    else:
                        configs[n] += 1
                elif event.key == pygame.K_LEFT:  
                    if configs[n] == 0:
                        configs[n] = 2
                    else:
                        configs[n] -= 1
                elif event.key == pygame.K_q:     
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_j: 
                    stop = 1
            draw_config(configs)    

##
## Snake class
##

class Snake:
    def __init__(self):

        # Dimension of each snake segment.

        self.x, self.y = size[configs[1]], size[configs[1]]

        # Initial direction
        # xmov :  -1 left,    0 still,   1 right
        # ymov :  -1 up       0 still,   1 dows
        self.xmov = 1
        self.ymov = 0

        # The snake has a head segement,
        self.head = pygame.Rect(self.x, self.y, size[configs[1]], size[configs[1]])

        # and a tail (array of segments).
        self.tail = []

        # The snake is born.
        self.alive = True

        # No collected apples.
        self.got_apple = False

        
    # This function is called at each loop interation.

    def update(self):
        global apple

        # Check for border crash.
        if self.head.x not in range(0, WIDTH) or self.head.y not in range(0, HEIGHT):
            self.alive = False

        # Check for self-bite.
        for square in self.tail:
            if self.head.x == square.x and self.head.y == square.y:
                self.alive = False

        # In the event of death, reset the game arena.
        if not self.alive:

            # Tell the bad news
            pygame.draw.rect(arena, DEAD_HEAD_COLOR, snake.head)
            center_prompt("Game Over", "Press to restart")

            # Respan the head
            self.x, self.y = size[configs[1]], size[configs[1]]
            self.head = pygame.Rect(self.x, self.y, size[configs[1]], size[configs[1]])

            # Respan the initial tail
            self.tail = []

            # Initial direction
            self.xmov = 1 # Right
            self.ymov = 0 # Still

            # Resurrection
            self.alive = True
            self.got_apple = False

            # Drop an apple
            apple = Apple()


        # Move the snake.

        # If head hasn't moved, tail shouldn't either (otherwise, self-byte).
        if (self.xmov or self.ymov):

            # Prepend a new segment to tail.
            self.tail.insert(0,pygame.Rect(self.head.x, self.head.y, size[configs[1]], size[configs[1]]))

            if self.got_apple:
                self.got_apple = False 
            else:
                self.tail.pop()


            # Move the head along current direction.
            self.head.x += self.xmov * size[configs[1]]
            self.head.y += self.ymov * size[configs[1]]

##
## The apple class.
##

class Apple:
    def __init__(self):

        # Pick a random position within the game arena
        self.x = int(random.randint(0, WIDTH)/size[configs[1]]) * size[configs[1]]
        self.y = int(random.randint(0, HEIGHT)/size[configs[1]]) * size[configs[1]]

        # Create an apple at that location
        self.rect = pygame.Rect(self.x, self.y, size[configs[1]], size[configs[1]])

    # This function is called each interation of the game loop

    def update(self):

        # Drop the apple
        pygame.draw.rect(arena, APPLE_COLOR, self.rect)


##
## Draw the arena
##

def draw_grid():
    for x in range(0, WIDTH, size[configs[1]]):
        for y in range(0, HEIGHT, size[configs[1]]):
            rect = pygame.Rect(x, y, size[configs[1]], size[configs[1]])
            pygame.draw.rect(arena, GRID_COLOR, rect, 1)

score = BIG_FONT.render("1", True, MESSAGE_COLOR)
score_rect = score.get_rect(center=(WIDTH/2, HEIGHT/20+HEIGHT/30))

draw_grid()

snake = Snake()    # The snake

apple = Apple()    # An apple

center_prompt(WINDOW_TITLE, "Press to start")

##
## Main loop
##

while True:

    for event in pygame.event.get():           # Wait for events

       # App terminated
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

          # Key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:    # Down arrow:  move down
                snake.ymov = 1
                snake.xmov = 0
            elif event.key == pygame.K_UP:    # Up arrow:    move up
                snake.ymov = -1
                snake.xmov = 0
            elif event.key == pygame.K_RIGHT: # Right arrow: move right
                snake.ymov = 0
                snake.xmov = 1
            elif event.key == pygame.K_LEFT:  # Left arrow:  move left
                snake.ymov = 0
                snake.xmov = -1
            elif event.key == pygame.K_q:     # Q         : quit game
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_p:     # S         : pause game
                game_on = not game_on

    ## Update the game

    if game_on:

        snake.update()

        arena.fill(ARENA_COLOR)
        draw_grid()

        apple.update()
        
    # Draw the tail
    for square in snake.tail:
        pygame.draw.rect(arena, TAIL_COLOR, square)

    # Draw head
    pygame.draw.rect(arena, HEAD_COLOR, snake.head)

    # Show score (snake length = head + tail)
    score = BIG_FONT.render(f"{len(snake.tail)}", True, SCORE_COLOR)
    arena.blit(score, score_rect)

    # If the head pass over an apple, lengthen the snake and drop another apple
    if snake.head.x == apple.x and snake.head.y == apple.y:
        #snake.tail.append(pygame.Rect(snake.head.x, snake.head.y, configs[1].value, configs[1].value))
        snake.got_apple = True;
        apple = Apple()


    # Update display and move clock.
    pygame.display.update()
    clock.tick(velocity[configs[0]])
