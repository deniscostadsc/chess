try:
    import unittest2 as unittest
except ImportError:
    import unittest

from chess.board import Board
from chess.pieces import King, Rook, Queen, ImpossibleMove, Pawn, Knight


class TestBoard(unittest.TestCase):
    def test_instantiate_board(self):
        board = Board()
        self.assertEqual(64, len(board.squares))

        pieces = [piece for piece in board.squares.values() if piece is not None]
        self.assertEqual(32, len(pieces))

    def test_board_regular_move(self):
        board = Board()
        knight = board.squares['g1']
        board.move('g1', 'f3')
        self.assertIs(knight, board.squares['f3'])
        self.assertIsNone(board.squares['g1'])

        board = Board()
        pawn = board.squares['e2']
        board.move('e2', 'e3')
        self.assertIs(pawn, board.squares['e3'])
        self.assertIsNone(board.squares['e2'])

    def test_impossible_move(self):
        board = Board()
        self.assertRaises(ImpossibleMove, board.move, 'g1', 'g3')
        self.assertRaises(ImpossibleMove, board.move, 'b2', 'b5')


class TestBoardCapture(unittest.TestCase):
    def test_knight_capture(self):
        board = Board(initial_pieces={'e5': Pawn('black'), 'f3': Knight('white')})
        pieces = [piece for piece in board.squares.values() if piece is not None]
        self.assertEqual(2, len(pieces))

        knight = board.squares['f3']
        board.move('f3', 'e5')
        self.assertIs(knight, board.squares['e5'])

        pieces = [piece for piece in board.squares.values() if piece is not None]
        self.assertEqual(1, len(pieces))

    def test_fail_knight_capture_ally(self):
        board = Board(initial_pieces={'e5': Pawn('white'), 'f3': Knight('white')})
        self.assertRaises(ImpossibleMove, board.move, 'f3', 'e5')

    def test_bishop_capture_rook(self):
        board = Board()
        pieces = [piece for piece in board.squares.values() if piece is not None]
        self.assertEqual(32, len(pieces))

        bishop = board.squares['f1']
        board.move('g2', 'g3')  # white pawn moves
        board.move('b7', 'b6')  # black pawn moves
        board.move('f1', 'g2')  # white bishop moves
        board.move('g8', 'f6')  # black knight moves
        board.move('g2', 'a8')  # white bishop capture white rook
        self.assertIs(bishop, board.squares['a8'])

        pieces = [piece for piece in board.squares.values() if piece is not None]
        self.assertEqual(31, len(pieces))


class TestBoardExceptionMoves(unittest.TestCase):
    def test_pawn_moves_two_square(self):
        board = Board()
        pawn = board.squares['a2']
        board.move('a2', 'a4')
        self.assertIs(pawn, board.squares['a4'])
        self.assertIsNone(board.squares['a2'])

    def test_fail_pawn_moves_two_squares(self):
        board = Board()
        board.move('a2', 'a3')
        self.assertRaises(ImpossibleMove, board.move, 'a3', 'a5')

    def test_castling_right_white(self):
        board = Board(initial_pieces={'e1': King('white'), 'h1': Rook('white')})
        king = board.squares['e1']
        rook = board.squares['h1']
        board.move('e1', 'g1')
        self.assertIs(king, board.squares['g1'])
        self.assertIs(rook, board.squares['f1'])
        self.assertIsNone(board.squares['e1'])
        self.assertIsNone(board.squares['h1'])

    def test_castling_left_white(self):
        board = Board(initial_pieces={'e1': King('white'), 'a1': Rook('white')})
        king = board.squares['e1']
        rook = board.squares['a1']
        board.move('e1', 'c1')
        self.assertIs(king, board.squares['c1'])
        self.assertIs(rook, board.squares['d1'])
        self.assertIsNone(board.squares['e1'])
        self.assertIsNone(board.squares['a1'])

    def test_castling_right_black(self):
        board = Board(initial_pieces={'e8': King('white'), 'h8': Rook('white')})
        king = board.squares['e8']
        rook = board.squares['h8']
        board.move('e8', 'g8')
        self.assertIs(king, board.squares['g8'])
        self.assertIs(rook, board.squares['f8'])
        self.assertIsNone(board.squares['e8'])
        self.assertIsNone(board.squares['h8'])

    def test_castling_left_black(self):
        board = Board(initial_pieces={'e8': King('white'), 'a8': Rook('white')})
        king = board.squares['e8']
        rook = board.squares['a8']
        board.move('e8', 'c8')
        self.assertIs(king, board.squares['c8'])
        self.assertIs(rook, board.squares['d8'])
        self.assertIsNone(board.squares['e8'])
        self.assertIsNone(board.squares['a8'])

    def test_fail_castling_when_rook_already_moved(self):
        board = Board(initial_pieces={'a7': Pawn('black'), 'e1': King('white'), 'h1': Rook('white')})
        board.move('h1', 'h8')
        board.move('a7', 'a6')  # pawn moves
        board.move('h8', 'h1')
        board.move('a6', 'a5')  # pawn moves
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g1')

    def test_fail_castling_when_king_already_moved(self):
        board = Board(initial_pieces={'a7': Pawn('black'), 'e1': King('white'), 'h1': Rook('white')})
        board.move('e1', 'f1')
        board.move('a7', 'a6')  # pawn moves
        board.move('f1', 'e1')
        board.move('a6', 'a5')  # pawn moves
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g1')

    def test_fail_castling_when_no_rook_involved(self):
        board = Board(initial_pieces={'e1': King('white'), 'h1': Queen('white')})
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g1')

    def test_fail_castling_when_is_not_same_line(self):
        board = Board(initial_pieces={'e1': King('white'), 'h2': Rook('white')})
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g2')

    def test_fail_castling_when_destiny_is_too_far(self):
        board = Board(initial_pieces={'e1': King('white'), 'a1': Rook('white')})
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'b1')

    def test_fail_castling_when_some_piece_is_between_king_rook(self):
        board = Board(initial_pieces={'e1': King('white'), 'f1': Queen('white'), 'h1': Rook('white')})
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g1')

    def test_fail_castling_when_pieces_are_black_and_white(self):
        board = Board(initial_pieces={'e1': King('white'), 'h1': Rook('black')})
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g1')

    def test_fail_castling_when_pieces_start_in_wrong_place(self):
        board = Board(initial_pieces={'e2': King('white'), 'h2': Rook('black')})
        self.assertRaises(ImpossibleMove, board.move, 'e2', 'g2')


class TestBoardGame(unittest.TestCase):
    def test_alternating_between_players(self):
        board = Board()
        self.assertEqual('white', board.turn)
        board.move('g2', 'g3')  # white pawn moves
        self.assertEqual('black', board.turn)
        board.move('b7', 'b6')  # black pawn moves
        self.assertEqual('white', board.turn)
        board.move('f1', 'g2')  # white bishop moves
        self.assertEqual('black', board.turn)
        board.move('g8', 'f6')  # black knight moves
        self.assertEqual('white', board.turn)
        board.move('g2', 'a8')  # white bishop capture white rook
        self.assertEqual('black', board.turn)

    def test_white_pieces_start_game(self):
        board = Board()
        self.assertEqual('white', board.turn)
        self.assertRaises(ImpossibleMove, board.move, 'b7', 'b6')  # black pawn try to move
