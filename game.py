import classes

global_x = 1  # Going one back or forward is one square in the 24 24 table 
global_y = 24 # Going one down or up is 24 squares in the 24 24 table
global_current_player = "J1"
global_list_of_walls = []
global_list_of_walls_p1 = []
global_list_of_walls_p2 = []


"""
board : 
[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
Each 0 corresponds to a element of the square class with the value 0
(1 or 2 if a player played on it)
"""

def create_board():
    board = []
    for i in range(0,25):
        line = []
        for j in range(0,25):
            line.append(classes.Square(i,j,0))
        board.append(line)
        
    return board

def print_board(board):
    for line in range(0, len(board)):
        printline = ""
        for col in range(0,len(board[line])):
            printline = printline + str(board[line][col].player_occupying) + " "
        print(printline)

def tower_can_be_placed(board, x, y):
    # check if the square is empty
    if board[x][y].player_occupying == 0:
        return True
    else:
        return False

def place_tower(board, x, y):
    if tower_can_be_placed(board, x, y):
        if global_current_player == "J1":
            board[x][y].player_occupying = 1
        else:
            board[x][y].player_occupying = 2
        return True
    else:
        return False
        
def test_wall_blocking_right_up_up(x, y):
    for wall in global_list_of_walls:
        if classes.Wall(classes.Square(x-1, y-1, 1), classes.Square(x, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-1, y, 1), classes.Square(x, y+2, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-2, y-1, 1), classes.Square(x-1, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-2, y, 1), classes.Square(x-1, y+2, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-3, y, 1), classes.Square(x-1, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-2, y, 1), classes.Square(x, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-1, y, 1), classes.Square(x+1, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-1,y, 1), classes.Square(x-2, y+2, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x, y-1, 1), classes.Square(x-1, y+1, 1), 1).equals(wall):
            return False
    return True

def test_wall_blocking_right_down_down(x, y):
    for wall in global_list_of_walls:
        if classes.Wall(classes.Square(x+2, y, 1), classes.Square(x, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+2, y, 1), classes.Square(x+1, y+2, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y-1, 1), classes.Square(x, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y, 1), classes.Square(x-1, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y, 1), classes.Square(x, y+2, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y, 1), classes.Square(x+2, y+2, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y+1, 1), classes.Square(x, y-1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y+1, 1), classes.Square(x+2, y-1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y+1, 1), classes.Square(x+3, y, 1), 1).equals(wall):
            return False
    return True

def test_wall_blocking_right_right_up(x, y):
    for wall in global_list_of_walls:
        if classes.Wall(classes.Square(x-1, y, 1), classes.Square(x+1, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-1, y+1, 1), classes.Square(x+1, y+2, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-2, y, 1), classes.Square(x, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-2, y+1, 1), classes.Square(x, y+2, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-1, y-1, 1), classes.Square(x, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-1, y, 1), classes.Square(x, y+2, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-1, y+1, 1), classes.Square(x, y+3, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y, 1), classes.Square(x-1, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x, y+1, 1), classes.Square(x-2, y+2, 1), 1).equals(wall):
            return False
    return True

def test_wall_blocking_right_right_down(x, y):
    for wall in global_list_of_walls:
        if classes.Wall(classes.Square(x, y+2, 1), classes.Square(x+1, y, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-1, y+1, 1), classes.Square(x+1, y, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x, y+2, 1), classes.Square(x+2, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x-1, y, 1), classes.Square(x+1, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y+1, 1), classes.Square(x-1, y+2, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y-1, 1), classes.Square(x, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+2, y, 1), classes.Square(x, y+1, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x+1, y+1, 1), classes.Square(x, y+3, 1), 1).equals(wall):
            return False
        if classes.Wall(classes.Square(x, y+1, 1), classes.Square(x+2, y+2, 1), 1).equals(wall):
            return False
    return True

def place_Wall(board, x, y):
    # We place a wall if the towers are the same color, and after testing that other walls aren't making the placement impossible, add it to the list of walls
    # There are 8 squares to test, and 4 different wall positions :
    # O X    X O     O X X     X X O     
    # X\X    X/X      -\_       _/-
    # X O    O X     X X O     O X X
    list_of_walls_created = []
    if x >= 2 and y <= 22:
        if board[x][y].player_occupying == board[x-2][y+1].player_occupying:
            if test_wall_blocking_right_up_up(x, y):
                list_of_walls_created.append(board[x-2][y+1])
                global_list_of_walls.append(classes.Wall(board[x-2][y+1], board[x][y], board[x][y].player_occupying))
              #  print("Wall placed at : " + str(x-2) + "," + str(y+1) + " --- " + str(x) + "," + str(y))
                if board[x][y].player_occupying == 1:
                    global_list_of_walls_p1.append(classes.Wall(board[x-2][y+1], board[x][y], board[x][y].player_occupying))
                else:
                    global_list_of_walls_p2.append(classes.Wall(board[x-2][y+1], board[x][y], board[x][y].player_occupying))
 
    if x <= 21 and y >= 1:
        if board[x][y].player_occupying == board[x+2][y-1].player_occupying:
            if test_wall_blocking_right_up_up(x+2, y-1):
                list_of_walls_created.append(board[x+2][y-1])
                global_list_of_walls.append(classes.Wall(board[x+2][y-1], board[x][y], board[x][y].player_occupying))
               # print("Wall placed at : " + str(x+2) + "," + str(y-1) + " --- " + str(x) + "," + str(y))
                if board[x][y].player_occupying == 1:
                    global_list_of_walls_p1.append(classes.Wall(board[x+2][y-1], board[x][y], board[x][y].player_occupying))
                else:
                    global_list_of_walls_p2.append(classes.Wall(board[x+2][y-1], board[x][y], board[x][y].player_occupying))
                
    if x <= 21 and y <= 22:
        if board[x][y].player_occupying == board[x+2][y+1].player_occupying:
            if test_wall_blocking_right_down_down(x, y):
                global_list_of_walls.append(classes.Wall(board[x][y], board[x+2][y+1], board[x][y].player_occupying))
                list_of_walls_created.append(board[x+2][y+1])
                if board[x][y].player_occupying == 1:
                    global_list_of_walls_p1.append(classes.Wall(board[x][y], board[x+2][y+1], board[x][y].player_occupying))
                else:
                    global_list_of_walls_p2.append(classes.Wall(board[x][y], board[x+2][y+1], board[x][y].player_occupying))
                #print("Wall placed at : " + str(x) + "," + str(y) + " --- " + str(x+2) + "," + str(y+1))

    if x >= 2 and y >= 1:
        if board[x][y].player_occupying == board[x-2][y-1].player_occupying:
            if test_wall_blocking_right_down_down(x-2, y-1):
                global_list_of_walls.append(classes.Wall(board[x-2][y-1], board[x][y], board[x][y].player_occupying))
                list_of_walls_created.append(board[x-2][y-1])
                if board[x][y].player_occupying == 1:
                    global_list_of_walls_p1.append(classes.Wall(board[x-2][y-1], board[x][y], board[x][y].player_occupying))
                else:
                    global_list_of_walls_p2.append(classes.Wall(board[x-2][y-1], board[x][y], board[x][y].player_occupying))
                #print("Wall placed at : " + str(x-2) + "," + str(y-1) + " --- " + str(x) + "," + str(y))

    if x <= 22 and y <= 21:
        if board[x][y].player_occupying == board[x+1][y+2].player_occupying:
            if test_wall_blocking_right_right_down(x, y):
                list_of_walls_created.append(board[x+1][y+2])
                global_list_of_walls.append(classes.Wall(board[x][y], board[x+1][y+2], board[x][y].player_occupying))
                if board[x][y].player_occupying == 1:
                    global_list_of_walls_p1.append(classes.Wall(board[x][y], board[x+1][y+2], board[x][y].player_occupying))
                else:
                    global_list_of_walls_p2.append(classes.Wall(board[x][y], board[x+1][y+2], board[x][y].player_occupying))
                #print("Wall placed at : " + str(x) + "," + str(y) + " --- " + str(x+1) + "," + str(y+2))

    if x >= 1 and y >= 2:
        if board[x][y].player_occupying == board[x-1][y-2].player_occupying:
            if test_wall_blocking_right_right_down(x-1, y-2):
                global_list_of_walls.append(classes.Wall(board[x-1][y-2], board[x][y], board[x][y].player_occupying))
                list_of_walls_created.append(board[x-1][y-2])
                if board[x][y].player_occupying == 1:
                    global_list_of_walls_p1.append(classes.Wall(board[x-1][y-2], board[x][y], board[x][y].player_occupying))
                else:
                    global_list_of_walls_p2.append(classes.Wall(board[x-1][y-2], board[x][y], board[x][y].player_occupying))
#                print("Wall placed at : " + str(x-1) + "," + str(y-2) + " --- " + str(x) + "," + str(y))


    if x <= 22 and y >= 2:
        if board[x][y].player_occupying == board[x+1][y-2].player_occupying:
            if test_wall_blocking_right_right_up(x+1, y-2):
                global_list_of_walls.append(classes.Wall(board[x][y], board[x+1][y-2], board[x][y].player_occupying))
                list_of_walls_created.append(board[x+1][y-2])
                if board[x][y].player_occupying == 1:
                    global_list_of_walls_p1.append(classes.Wall(board[x][y], board[x+1][y-2], board[x][y].player_occupying))
                else:
                    global_list_of_walls_p2.append(classes.Wall(board[x][y], board[x+1][y-2], board[x][y].player_occupying))
           #     print("Wall placed at : " + str(x) + "," + str(y) + " --- " + str(x+1) + "," + str(y-2))

    if x >= 1 and y <= 21:
        if board[x][y].player_occupying == board[x-1][y+2].player_occupying:
            if test_wall_blocking_right_right_up(x, y):
                global_list_of_walls.append(classes.Wall(board[x-1][y+2], board[x][y], board[x][y].player_occupying))
                list_of_walls_created.append(board[x-1][y+2])
                if board[x][y].player_occupying == 1:
                    global_list_of_walls_p1.append(classes.Wall(board[x-1][y+2], board[x][y], board[x][y].player_occupying))
                else:
                    global_list_of_walls_p2.append(classes.Wall(board[x-1][y+2], board[x][y], board[x][y].player_occupying))
               # print("Wall placed at : " + str(x-1) + "," + str(y+2) + " --- " + str(x) + "," + str(y))

    return list_of_walls_created

def switch_player():
    # switch the turn of the player
    global global_current_player
    if global_current_player == "J1":
        global_current_player = "J2"
       # print("It is your turn, " + global_current_player)

    else:
        global_current_player = "J1"
      #  print("It is your turn, " + global_current_player)