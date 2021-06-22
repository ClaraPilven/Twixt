class Square:
  def __init__(self, x_coordinates, y_coordinates, player_occupying):
    self.x_coordinates = x_coordinates
    self.y_coordinates = y_coordinates
    self.player_occupying = player_occupying

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