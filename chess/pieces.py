from abc import ABCMeta

from chess import x, y


class InvalidChessColor(Exception):
    pass


class DiagonalMove(object):
    '''Mixin that implements diagonal move.
    '''

    __metaclass__ = ABCMeta

    def can_move_diagonally(self, source, destination):
        return abs(x.index(source[0]) - x.index(destination[0])) == abs(y.index(destination[1]) - y.index(source[1]))


class VerticalAndHorizontalMove(object):
    '''Mixin that implements vertical and horizontal move.
    '''

    __metaclass__ = ABCMeta

    def can_move_vertically_or_horizontally(self, source, destination):
        horizontal = x.index(source[0]) == x.index(destination[0]) and y.index(source[1]) != y.index(destination[1])
        vertical = x.index(source[0]) != x.index(destination[0]) and y.index(source[1]) == y.index(destination[1])

        return horizontal or vertical


class Piece(object):
    def __init__(self, color):
        color = color.lower()

        if color not in ['white', 'black']:
            raise InvalidChessColor('That color should be "black" or "white".')

        self.__color = color
        self.__moved = False

    @property
    def name(self):
        return '%s %s' % (self.color.capitalize(), self.__class__.__name__)

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


class Bishop(Piece, DiagonalMove):
    def can_move(self, source, destination):
        return self.can_move_diagonally(source, destination)


class Rook(Piece, VerticalAndHorizontalMove):
    def can_move(self, source, destination):
        return self.can_move_vertically_or_horizontally(source, destination)


class King(Piece):
    def can_move(self, source, destination):
        x_distance = abs(x.index(source[0]) - x.index(destination[0]))
        y_distance = abs(y.index(source[1]) - y.index(destination[1]))

        return x_distance in [0, 1] and y_distance in [0, 1] and x_distance + y_distance != 0


class Queen(Piece, DiagonalMove, VerticalAndHorizontalMove):
    def can_move(self, source, destination):
        return (self.can_move_diagonally(source, destination) or
                self.can_move_vertically_or_horizontally(source, destination))


class Pawn(Piece):
    def can_move(self, source, destination):
        if self.color == 'white' and x.index(source[0]) == x.index(destination[0]):
            ordinary_move = y.index(destination[1]) - y.index(source[1]) == 1
            two_square_move = not self.moved and y.index(destination[1]) - y.index(source[1]) == 2
            return ordinary_move or two_square_move

        if self.color == 'black' and x.index(source[0]) == x.index(destination[0]):
            ordinary_move = y.index(destination[1]) - y.index(source[1]) == -1
            two_square_move = not self.moved and y.index(destination[1]) - y.index(source[1]) == -2
            return ordinary_move or two_square_move
        return False


class Knight(Piece):
    def can_move(self, source, destination):
        x_distance = abs(x.index(source[0]) - x.index(destination[0]))
        y_distance = abs(y.index(source[1]) - y.index(destination[1]))

        return x_distance in [1, 2] and y_distance in [1, 2] and x_distance != y_distance
