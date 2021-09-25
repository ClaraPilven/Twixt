#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:08:00 2021

@author: clarapilven
"""
import button
import game
import random
import pygame as pg

def drawline(surface, button1, button2):
    color = pg.Color("Blue")
    pg.draw.line(surface, color, [27.5+button1.y_coordinates*25, 27.5+button1.x_coordinates*25+50], \
                 [button2.y_coordinates*25+27.5, button2.x_coordinates*25+27.5+50], 2)
    

def make_move(screen, board):
    i = random.randint(0,23)    
    j = random.randint(0,23)
    
    move_made = False
    while move_made is not True:
        if game.tower_can_be_placed(board, i, j):
            move_made = True
        else:
            i = random.randint(0,23)    
            j = random.randint(0,23)
    
    game.place_tower(board, i, j)
    list_walls = game.place_Wall(board, i, j)
    for wall in list_walls:
        drawline(screen, board[i][j], wall)
    #print(str(i) + " " + str(j))
    game.switch_player()
    return i, j