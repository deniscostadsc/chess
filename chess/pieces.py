from chess import x, y


class InvalidChessColor(Exception):
    pass


class Piece(object):
    def __init__(self, color):
        color = color.lower()

        if color not in ['white', 'black']:
            raise InvalidChessColor('That color should be "black" or "white".')

        self.__color = color
        self.__moved = False

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def color(self):
        return self.__color

    @property
    def moved(self):
        return self.__moved

    @moved.setter
    def moved(self, value):
        if not self.__moved and value is True:
            self.__moved = value


class Bishop(Piece):
    def can_move(self, _from, to):
        return abs(x.index(_from[0]) - x.index(to[0])) == abs(y.index(to[1]) - y.index(_from[1]))


class Rook(Piece):
    def can_move(self, _from, to):
        horizontal = x.index(_from[0]) == x.index(to[0]) and y.index(_from[1]) != y.index(to[1])
        vertical = x.index(_from[0]) != x.index(to[0]) and y.index(_from[1]) == y.index(to[1])

        return bool(horizontal or vertical)


class King(Piece):
    def can_move(self, _from, to):
        x_distance = abs(x.index(_from[0]) - x.index(to[0]))
        y_distance = abs(y.index(_from[1]) - y.index(to[1]))

        return bool(x_distance in [0, 1] and y_distance in [0, 1] and x_distance + y_distance != 0)


class Queen(Piece):
    def can_move(self, _from, to):
        # move as a Rook {{
        horizontal = x.index(_from[0]) == x.index(to[0]) and y.index(_from[1]) != y.index(to[1])
        vertical = x.index(_from[0]) != x.index(to[0]) and y.index(_from[1]) == y.index(to[1])

        if horizontal or vertical:
            return True
        # }}

        # move as a Bishop {{
        return abs(x.index(_from[0]) - x.index(to[0])) == abs(y.index(to[1]) - y.index(_from[1]))
        # }}


class Pawn(Piece):
    def can_move(self, _from, to):
        if (self.color == 'white' and x.index(_from[0]) == x.index(to[0]) and
                y.index(to[1]) - y.index(_from[1]) == 1):
            return True

        return (self.color == 'black' and x.index(_from[0]) == x.index(to[0]) and
                y.index(to[1]) - y.index(_from[1]) == -1)


class Knight(Piece):
    def can_move(self, _from, to):
        x_distance = abs(x.index(_from[0]) - x.index(to[0]))
        y_distance = abs(y.index(_from[1]) - y.index(to[1]))

        return x_distance in [1, 2] and y_distance in [1, 2] and x_distance != y_distance
