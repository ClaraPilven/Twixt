import pygame as pg
class Square:
    def __init__(self, x_coordinates, y_coordinates, player_occupying):
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.player_occupying = player_occupying
        
    def equals(self, square):
        if self.x_coordinates == square.x_coordinates and self.y_coordinates == square.y_coordinates and self.player_occupying == square.player_occupying:
            return True
        return False
    
    def print_square(self):
        print("Square : " + str(self.x_coordinates) + "," + str(self.y_coordinates) + "  " + str(self.player_occupying))
        
class Wall:
    def __init__(self, s1, s2, player_occupying):
        self.square1 = s1
        self.square2 = s2
        self.player_occupying = player_occupying

    def equals(self, wall):
        if self.square1.x_coordinates == wall.square1.x_coordinates and self.square1.y_coordinates == wall.square1.y_coordinates and \
        self.square2.x_coordinates == wall.square2.x_coordinates and self.square2.y_coordinates == wall.square2.y_coordinates:
            return True
        if self.square2.x_coordinates == wall.square1.x_coordinates and self.square2.y_coordinates == wall.square1.y_coordinates and \
        self.square1.x_coordinates == wall.square2.x_coordinates and self.square1.y_coordinates == wall.square2.y_coordinates:
            return True
        return False
        
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = pg.font.Font(None, 32).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        nickname = ""
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    nickname = self.text
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = pg.font.Font(None, 32).render(self.text, True, self.color)
        return nickname
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)