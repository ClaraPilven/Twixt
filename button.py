#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:18:03 2021

@author: clarapilven
"""

import pygame as pg
import game
import random
import check_victory

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pg.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),)
        
        if self.text != '':
            font = pg.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
 
class Tower():
    def __init__(self, i, j, x, y, width, height):
        self.color = pg.Color("Grey")
        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clicked = False
        self.rect = pg.Rect(x, y, width, height)
        
    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pg.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def get_event(self, event, surface, board):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            return self.on_click(event, surface, board)
                
    def on_click(self, event, surface, board):
        if not self.clicked:
            self.clicked = True
            if self.rect.collidepoint(pg.mouse.get_pos()):
                return self.print_on_press(board, self.i, self.j, surface)
        self.clicked = False  

    def drawline(self, surface, button1, button2):
        color = self.color
        pg.draw.line(surface, color, [27.5+button1.y_coordinates*25, 27.5+button1.x_coordinates*25+50], \
                     [button2.y_coordinates*25+27.5, button2.x_coordinates*25+27.5+50], 2)

    def print_on_press(self, board, i, j, surface):
        if self.color == pg.Color("Grey"):
           #     print(str(i) + " " + str(j))
            if game.global_current_player == "J1":            
                self.color = pg.Color("Red")
            else:
                self.color = pg.Color("Blue")
            game.place_tower(board, i, j)
            list_walls = game.place_Wall(board, i, j)
            for wall in list_walls:
                self.drawline(surface, board[i][j], wall)
            if game.global_current_player == "J1":
                if check_victory.game_is_won_p1(game.global_list_of_walls_p1):
                    return True
            else:
                if check_victory.game_is_won_p2(game.global_list_of_walls_p2):
                    return True
            game.switch_player()
        return False
    
    def make_move(self, screen, board):
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
            self.drawline(screen, board[i][j], wall)
        game.switch_player()