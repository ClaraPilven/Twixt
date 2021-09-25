#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:47:45 2021

@author: clarapilven
"""

import button
import gamepage
import gamepage_ai
import pygame

def main():
    pygame.init()
    homepage()
    pygame.quit()

#%%

def redraw_window(green_button, red_button, quit_button, game_image):
    
    screen = pygame.display.set_mode((500, 500))
    screen.fill((255,255,255))
    screen.blit(game_image, (50,50))
    green_button.draw(screen, (0,0,0))
    quit_button.draw(screen, (0,0,0))
    red_button.draw(screen, (0,0,0))
    
def homepage():

    run = True
    screen = pygame.display.set_mode((500, 500))
    game_image = pygame.image.load("/home/clarapilven/Twixt_v2/images/Twixt_homepage_image.jpg").convert_alpha()
    green_button = button.Button((0,255,0), 75, 380, 150, 70, 'VS Computer')
    red_button = button.Button((255,0,0), 275, 380, 150, 70, 'VS Player')
    quit_button = button.Button((255,255,255), 175, 460, 150, 30, 'Leave Game')
    playing = 0

    
    while run:
        redraw_window(green_button, red_button, quit_button, game_image)
        pygame.display.update()        
            
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()    
    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if green_button.isOver(pos):
                    playing = 1
                    print("Playing against the Computer")
                    run = False
                if red_button.isOver(pos):
                    playing = 2
                    print("Playing against a player")
                    run = False
                if quit_button.isOver(pos):
                    playing = 0
                    print("Quitting Game")
                    run = False

    
    if playing == 0:
        pygame.quit()
    elif playing == 1:
        gamepage_ai.game_screen(screen)
        pygame.quit()
    elif playing == 2:
        gamepage.game_screen(screen)
        pygame.quit()

if __name__ == "__main__":
    main()
