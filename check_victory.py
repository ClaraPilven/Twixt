#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: clarapilven
"""

def square_to_string(square):
    square_x = square.x_coordinates
    square_y = square.y_coordinates
    return str(square_x) + "" + str(square_y)

def get_neighbours_of_tower(tower, list_of_walls):
    list_of_neighbours = []
    for wall in list_of_walls:
        if tower.equals(wall.square1):
            list_of_neighbours.append(square_to_string(wall.square2))
        elif tower.equals(wall.square2):
            list_of_neighbours.append(square_to_string(wall.square1))
    return list_of_neighbours

def squares_to_dict(list_of_walls): # dict : key=Towercoordinates, value = ([neighbour_towers])
    square_dict = {}
    for wall in list_of_walls:
        key = square_to_string(wall.square1)
        value = (get_neighbours_of_tower(wall.square1, list_of_walls))
        square_dict[key] = value
        
        key = square_to_string(wall.square2)
        value = (get_neighbours_of_tower(wall.square2, list_of_walls))
        square_dict[key] = value
        
    return square_dict

def next_wall_p1(G, s):
    p1_win = ['230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '2310', '2311', '2312', '2313', '2314', '2315', '2316', '2317', '2318', '2319', '2320', '2321', '2322', '2323']
    color = dict()
    for v in G: color[v] = "white"
    P = dict()
    P[s] = None
    color[s]='grey'
    Q=[s]
    while Q:
        u=Q[-1]
        R=[y for y in G[u] if color[y]=='white']
        if R:
            if R[0] in p1_win: # TODO same as p2
                return True
            v=R[0]
            color[v]='grey'
            P[v]=u
            Q.append(v)
        else:
            Q.pop()
            color[u]='black'
    return False

def game_is_won_p1(list_of_walls):
    # check if the placement of this tower and walls implies a win
    for wall in list_of_walls:
        if wall.square1.x_coordinates == 0:
            return next_wall_p1(squares_to_dict(list_of_walls), square_to_string(wall.square1))
    return False

def next_wall_p2(G, s):
    p2_win = ['023', '123', '223', '323', '423', '523', '623', '723', '823', '923', '1023', '1123', '1223', '1323', '1423', '1523', '1623', '1723', '1823', '1923', '2023', '2123', '2223', '2323']
    color = dict()
    for v in G: color[v] = "white"
    P = dict()
    P[s] = None
    color[s]='grey'
    Q=[s]
    while Q:
        u=Q[-1]
        R=[y for y in G[u] if color[y]=='white']
        if R:
            if R[0] in p2_win:
                return True
            v=R[0]
            color[v]='grey'
            P[v]=u
            Q.append(v)
        else:
            Q.pop()
            color[u]='black'
    return False

def game_is_won_p2(list_of_walls):
    # TODO : check if the placement of this tower and walls implies a win
    for wall in list_of_walls:
        if wall.square1.y_coordinates == 0:
            return next_wall_p2(squares_to_dict(list_of_walls), square_to_string(wall.square1))
        elif wall.square2.y_coordinates == 0:
            return next_wall_p2(squares_to_dict(list_of_walls), square_to_string(wall.square2))

    return False

#list_walls_p1_win = []
#list_walls_p1_win.append(classes.Wall(classes.Square(0,0,1), classes.Square(2,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(4,0,1), classes.Square(6,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(2,0,1), classes.Square(4,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(6,0,1), classes.Square(8,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(8,0,1), classes.Square(10,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(10,0,1), classes.Square(12,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(12,0,1), classes.Square(14,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(14,0,1), classes.Square(16,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(16,0,1), classes.Square(18,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(18,0,1), classes.Square(20,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(20,0,1), classes.Square(22,0,1), 1))
#list_walls_p1_win.append(classes.Wall(classes.Square(22,0,1), classes.Square(23,0,1), 1))

#list_walls_p2_win = []
#
#list_walls_p2_win.append(classes.Wall(classes.Square(0,0,1), classes.Square(0,2,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,2,1), classes.Square(0,4,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,4,1), classes.Square(0,6,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,6,1), classes.Square(0,8,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,8,1), classes.Square(0,10,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,10,1), classes.Square(0,12,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,12,1), classes.Square(0,14,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,14,1), classes.Square(0,16,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,16,1), classes.Square(0,18,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,18,1), classes.Square(0,20,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,20,1), classes.Square(0,22,1), 1))
#list_walls_p2_win.append(classes.Wall(classes.Square(0,22,1), classes.Square(0,23,1), 1))
#
##print(game_is_won_p1(list_walls_p1_win))
#print(game_is_won_p2(list_walls_p2_win))