from chess.pieces import Rook, Knight, Bishop, Queen, King, Pawn
from chess import x, y


class ImpossibleMove(Exception):
    pass


class Board(object):
    def __init__(self, initial_pieces=None):
        self.check = None
        self.__turn = 'white'
        self.__squares = {}
        self.__initial_pieces = initial_pieces or {
            'a1': Rook('white'),
            'b1': Knight('white'),
            'c1': Bishop('white'),
            'd1': Queen('white'),
            'e1': King('white'),
            'f1': Bishop('white'),
            'g1': Knight('white'),
            'h1': Rook('white'),
            'a2': Pawn('white'),
            'b2': Pawn('white'),
            'c2': Pawn('white'),
            'd2': Pawn('white'),
            'e2': Pawn('white'),
            'f2': Pawn('white'),
            'g2': Pawn('white'),
            'h2': Pawn('white'),

            'a8': Rook('black'),
            'b8': Knight('black'),
            'c8': Bishop('black'),
            'd8': Queen('black'),
            'e8': King('black'),
            'f8': Bishop('black'),
            'g8': Knight('black'),
            'h8': Rook('black'),
            'a7': Pawn('black'),
            'b7': Pawn('black'),
            'c7': Pawn('black'),
            'd7': Pawn('black'),
            'e7': Pawn('black'),
            'f7': Pawn('black'),
            'g7': Pawn('black'),
            'h7': Pawn('black'),
        }

        for _x in x:
            for _y in y:
                self.__squares[_x + _y] = None
                if _x + _y in self.__initial_pieces:
                    self.__squares[_x + _y] = self.__initial_pieces[_x + _y]

    @property
    def turn(self):
        return self.__turn

    def get_piece(self, position):
        return self.__squares[position]

    def pieces_quantity(self):
        return len([piece for piece in self.__squares.values() if piece is not None])

    def is_tutorial_mode(self):
        # TODO: I have to improve this method!
        for piece in self.__squares.values():
            if isinstance(piece, King):
                return False
        return True

    def __is_castling(self, _from, to):
        y_from = _from[1]
        y_to = to[1]

        x_rook = 'a'
        between = ['b', 'c', 'd']
        if x.index(_from[0]) - x.index(to[0]) == -2:
            x_rook = 'h'
            between = ['f', 'g']

        king = self.get_piece(_from)
        rook = self.get_piece(x_rook + y_to)

        if not isinstance(rook, Rook):
            return False
        if y_from != y_to:
            return False
        if x.index(_from[0]) - x.index(to[0]) not in [-2, 2]:
            return False
        if king.moved or rook.moved:
            return False
        if king.color != rook.color:
            return False
        for _x in between:
            if self.get_piece(_x + y_to) is not None:
                return False

        return True

    def __move_castling(self, _from, to):
        y_to = to[1]

        x_rook = 'a'
        x_rook_to = 'd'
        if x.index(_from[0]) - x.index(to[0]) == -2:
            x_rook = 'h'
            x_rook_to = 'f'

        self.__squares[to], self.__squares[x_rook_to + y_to] = self.get_piece(_from), self.get_piece(x_rook + y_to)
        self.__squares[_from], self.__squares[x_rook + y_to] = None, None

        self.get_piece(to).moved = True
        self.get_piece(x_rook_to + y_to).moved = True

    def __switch_turn(self):
        self.__turn = 'white' if self.turn == 'black' else 'black'

    def __is_player_in_check(self, color, squares=None):

        other_color = 'black' if color == 'white' else 'white'
        squares = squares or self.__squares

        for position in squares:
            if isinstance(squares[position], King) and squares[position].color == color:
                king_position = position
                break

        for position in squares:
            if (squares[position] and
                    squares[position].color == other_color and
                    squares[position].can_move(position, king_position)):
                return True
        return False

    def move(self, _from, to):
        piece = self.get_piece(_from)
        destiny = self.get_piece(to)

        if piece.color != self.turn:
            raise ImpossibleMove("Not your turn!")
        if destiny is not None and destiny.color == piece.color:
            raise ImpossibleMove("You can't capture your ally!")

        if isinstance(piece, King):
            if self.__is_castling(_from, to):
                self.__move_castling(_from, to)
                return

        if not self.get_piece(_from).can_move(_from, to):
            raise ImpossibleMove("%s can't move to %s" % (self.get_piece(_from).name, to))

        piece.moved = True

        # check if player is getting out of check
        if self.check:
            # simulating movement
            _squares = dict(self.__squares)
            _squares[to], _squares[_from] = _squares[_from], None

            if not self.is_tutorial_mode() and self.__is_player_in_check(self.check, squares=_squares):
                raise ImpossibleMove('You should get out of check!')
            else:
                self.check = None

        self.__squares[to], self.__squares[_from] = self.get_piece(_from), None

        # check if player is putting opponent in check
        if not self.is_tutorial_mode() and self.__is_player_in_check('white' if self.turn == 'black' else 'black'):
            self.__switch_turn()
            self.check = self.turn
            return
        self.__switch_turn()
