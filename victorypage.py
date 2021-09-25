#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:23:45 2021

@author: clarapilven
"""
   
import button
import pygame
import game
import gamepage
import gamepage_ai
    
def redraw_window(screen, green_button, red_button, quit_button, game_image):
    green_button.draw(screen, (0,0,0))
    quit_button.draw(screen, (0,0,0))
    red_button.draw(screen, (0,0,0))
    
def victory(screen):
    
    run = True
    game_image = pygame.image.load("/home/clarapilven/Twixt_v2/images/Twixt_homepage_image.jpg").convert_alpha()
    green_button = button.Button((0,255,0), 140, 280, 150, 70, 'VS Computer')
    red_button = button.Button((255,0,0), 340, 280, 150, 70, 'VS Player')
    quit_button = button.Button((255,255,255), 240, 360, 150, 30, 'Leave Game')
    playing = 0

    
    while run:
        redraw_window(screen, green_button, red_button, quit_button, game_image)
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
        game.global_x = 1  # Going one back or forward is one square in the 24 24 table 
        game.global_y = 24 # Going one down or up is 24 squares in the 24 24 table
        game.global_current_player = "J1"
        game.global_list_of_walls = []
        game.global_list_of_walls_p1 = []
        game.global_list_of_walls_p2 = []
        gamepage_ai.game_screen(screen)
        pygame.quit()
    elif playing == 2:
        game.global_x = 1  # Going one back or forward is one square in the 24 24 table 
        game.global_y = 24 # Going one down or up is 24 squares in the 24 24 table
        game.global_current_player = "J1"
        game.global_list_of_walls = []
        game.global_list_of_walls_p1 = []
        game.global_list_of_walls_p2 = []
        gamepage.game_screen(screen)
        pygame.quit()