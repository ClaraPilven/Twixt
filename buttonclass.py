#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:40:01 2021

@author: matthieupilven
"""
import pygame as pg
import game
import classes
import check_victory

class Button(object):
    def __init__(self,  i, j, rect, **kwargs):
        self.rect = pg.Rect(rect)
        self.clicked = False
        self.hovered = False
        self.i = i
        self.j = j
        self.hover_text = None
        self.clicked_text = None
        self.process_kwargs(kwargs)
        self.render_text()
        
    def process_kwargs(self, kwargs):
        settings = {
                "color" : pg.Color('Grey'),
                "text" : None,
                "font" : pg.Color('Grey'),
                "call_on_release" : True,
                "hover_color" : None,
                "clicked_color" : None,
                "hover_font_color" : None,
                "clicked_font_color" : None,
                "font_color" : pg.Color("White"),
                "click_sound" : None,
                "hover_sound" : None,
                'border_color' : pg.Color("Black"),
                "border_hover_color" : pg.Color("Yellow"),
                "disabled" : False,
                'radius' : 3,
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)


    def print_on_press(self, board, i, j, surface):
        if self.color == pg.Color("Grey"):
            print(str(i) + " " + str(j))
            if game.global_current_player == "J1":            
                self.color = pg.Color("Red")
            else:
                self.color = pg.Color("Blue")
            game.place_tower(board, i, j)
            list_walls = game.place_Wall(board, i, j)
            for wall in list_walls:
                self.drawline(surface, board[i][j], wall)
            game.switch_player()
    
    
    def render_text(self):
        if self.text:
            if self.hover_font_color:
                color = self.hover_font_color
                self.hover_text = self.font.render(self.text, True, color)
            if self.clicked_font_color:
                color = self.clicked_font_color
                self.clicked_text = self.font.render(self.text, True, self.font_color)
        
    def get_event(self, event, surface):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event, surface)
    
    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if not self.call_on_release:
                self.function(self.i, self.j)
                
    def on_release(self, event, surface):
        if self.clicked and self.call_on_release:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.print_on_press(board, self.i, self.j, surface)
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                if self.hover_sound:
                    self.hover_sound.play()
        else:
            self.hovered = False
         
    def drawline(self, surface, button1, button2):
        color = self.color

        #top = i*btn_height + i*btn_spacing + spacer

        pg.draw.line(surface, color, [27.5+button1.y_coordinates*25, 27.5+button1.x_coordinates*25], \
                     [button2.y_coordinates*25+27.5, button2.x_coordinates*25+27.5], 2)
        
    def draw(self, surface):
        color = self.color
        text = self.text
        border = self.border_color
        self.check_hover()                
        if not self.disabled:
            if self.clicked and self.clicked_color:
                color = self.clicked_color
                if self.clicked_font_color:
                    text = self.clicked_text
                elif self.hovered and self.hover_color:
                    color = self.hover_color
                    if self.hover_font_color:
                        text = self.hover_text
                if self.hovered and not self.clicked:
                    border = self.border_hover_color
                
            if self.radius:
                rad = self.radius
            else:
                rad = 0
            self.round_rect(surface, self.rect, border, rad, 1, color)
                
    def round_rect(self, surface, rect, color, rad= 20, border=0, inside=(0,0,0,0)):
        rect = pg.Rect(rect)
        zeroed_rect = rect.copy()
        zeroed_rect.topleft = 0,0
        image = pg.Surface(rect.size).convert_alpha()
        image.fill((0,0,0,0))
        self._render_region(image, zeroed_rect, color, rad)
        if border:
            zeroed_rect.inflate_ip(-2*border, -2*border)
            self._render_region(image, zeroed_rect, inside, rad)
        surface.blit(image, rect)
        
    def _render_region(self, image, rect, color, rad):
        corners = rect.inflate(-2*rad, -2*rad)
        for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
            pg.draw.circle(image, color, getattr(corners, attribute), rad)
        image.fill(color, rect.inflate(-2*rad, 0))
        image.fill(color, rect.inflate(0, -2*rad))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def victory():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text("A PLAYER HAS WON", pg.font.SysFont(None, 20), (255,255,255), screen, 20, 20)
    
if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((530,530))
    screen_rect = screen.get_rect()
    done = False
            
    settings = {
        "clicked_font_color" : (0,0,0),
        'font' : pg.font.Font(None, 16),
        'font_color' : (200,100,255),
        'border_color' : (0,0,0),
    }
    
    board = game.create_board()

    
    btns = []
    for i in range(0, 20):
        for j in range(0, 20):
            btn_height = 15
            btn_width = 15
            spacer = 20
            btn_spacing = 10
            top = i*btn_height + i*btn_spacing + spacer
            left = j*btn_width + j*btn_spacing + spacer
            b = Button(i, j, rect=(left, top, btn_width, btn_height), text="a", **settings)
            btns.append(b)
    
    while not done:
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for btn in btns:
                btn.get_event(event, screen)
        for btn in btns:
            btn.draw(screen)
        pg.display.update()