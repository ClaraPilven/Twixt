#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:10:43 2021

@author: clarapilven
"""

import button
import game
import pygame as pg
import TwixtAI_v1_randomness
import homepage
import victorypage

def towers_creation():
    btns = []
    for i in range(0, 24):
        for j in range(0, 24):
            btn_height = 15
            btn_width = 15
            spacer = 20
            btn_spacing = 10
            top = i*btn_height + i*btn_spacing + spacer + 50
            left = j*btn_width + j*btn_spacing + spacer
            b = button.Tower(i, j, left, top, btn_width, btn_height)
            btns.append(b)
    return btns

def game_screen(screen):

    board = game.create_board()
    btns = towers_creation()

    screen = pg.display.set_mode((632,680))
    screen.fill((255,255,255))
    pg.display.update()

    pg.draw.line(screen, pg.Color("red"), [0,50],[630,50], 2)
    pg.draw.line(screen, pg.Color("red"), [0,680],[630,680], 2)
    pg.draw.line(screen, pg.Color("blue"), [0,50],[0,680], 2)
    pg.draw.line(screen, pg.Color("blue"), [628,50],[628,680], 2)

    return_button = button.Button((255,255,255), 10, 10, 80, 30, 'Return')

    run = True
    victory = False
    while run:
        action = 1
        return_button.draw(screen, (0,0,0))

        if game.global_current_player == "J2":
            i,j = TwixtAI_v1_randomness.make_move(screen, board)
            for btn in btns:
                if btn.i == i and btn.j == j:
                    btn.color = pg.Color("Blue")
        else:
            for event in pg.event.get():
                pos = pg.mouse.get_pos()
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if return_button.isOver(pos):
                        action = 1
                        print("Returning to homepage")
                        run = False
                    
                for btn in btns:
                    a_player_has_won = btn.get_event(event, screen, board)
                    if a_player_has_won:
                        victory = True
                if victory:
                    action = 2
                    run = False
        for btn in btns:
            btn.draw(screen)
        pg.display.update()

    if action == 1:
        homepage.homepage()
    elif action == 2:
        victorypage.victory(screen)