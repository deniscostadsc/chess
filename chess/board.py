from chess.pieces import Rook, Knight, Bishop, Queen, King, Pawn


class Board(object):
    def __init__(self, initial_pieces=None):
        self.__y = '12345678'
        self.__x = 'abcdefgh'
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

        for x in self.__x:
            for y in self.__y:
                self.__squares[x + y] = None
                if x + y in self.__initial_pieces:
                    self.__squares[x + y] = self.__initial_pieces[x + y]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def squares(self):
        return self.__squares

    def is_castling(self, _from, to):
        # y_from = _from[1]
        y_to = to[1]

        x_rook = 'a'
        # between = ['b', 'c', 'd']
        if self.__x.index(_from[0]) - self.__x.index(to[0]) == -2:
            x_rook = 'h'
            # between = ['f', 'g']

        king = self.squares[_from]
        rook = self.squares[x_rook + y_to]

        if not isinstance(rook, Rook):
            return False
        # if y_from != y_to:
        #     return False
        # if self.__x.index(_from[0]) - self.__x.index(to[0]) not in [-2, 2]:
        #     return False
        if king.moved or rook.moved:
            return False
        if king.color != rook.color:
            return False
        # for x in between:
        #     if self.squares[x + y_to] is not None:
        #         return False

        return True

    def move_castling(self, _from, to):
        y_to = to[1]

        x_rook = 'a'
        x_rook_to = 'd'
        if self.__x.index(_from[0]) - self.__x.index(to[0]) == -2:
            x_rook = 'h'
            x_rook_to = 'f'

        self.squares[to], self.squares[x_rook_to + y_to] = self.squares[_from], self.squares[x_rook + y_to]
        self.squares[_from], self.squares[x_rook + y_to] = None, None

    def is_valid_pawn_move(self, _from, to):
        if not self.squares[_from].moved:
            return self.x.index(_from[0]) == self.x.index(to[0]) and abs(self.y.index(to[1]) - self.y.index(_from[1])) == 2
        return False

    def move(self, _from, to):
        piece = self.squares[_from]
        if isinstance(piece, King):
            if self.is_castling(_from, to):
                self.move_castling(_from, to)
                return

        if isinstance(piece, Pawn):
            if self.is_valid_pawn_move(_from, to):
                self.squares[to], self.squares[_from] = self.squares[_from], None
                return

        self.squares[_from].move(_from, to)
        self.squares[to] = self.squares[_from]
        self.squares[_from] = None
