def next_wall_p1(square2, list_of_walls):
    for wall in list_of_walls:
        if wall.square1.x_coordinates == 23:
            return True
        if square2 == wall.square1:
            next_wall_p1(wall.square2, list_of_walls)
    return False

def game_is_won_p1(list_of_walls):
    # TODO : check if the placement of this tower and walls implies a win
    for wall in list_of_walls:
        if wall.square1.x_coordinates == 0:
            return next_wall_p1(wall.square2, list_of_walls)
    return False

def next_wall_p2(square2, list_of_walls):
    for wall in list_of_walls:
        if wall.square1.x_coordinates == 23:
            return True
        if square2 == wall.square1:
            next_wall_p1(wall.square2, list_of_walls)
    return False

def game_is_won_p2(list_of_walls):
    # TODO : check if the placement of this tower and walls implies a win
    for wall in list_of_walls:
        if wall.square1.x_coordinates == 0:
            return next_wall_p1(wall.square2, list_of_walls)
    return False