try:
    import unittest2 as unittest
except ImportError:
    import unittest

from chess.board import Board
from chess.pieces import King, Rook, Queen, ImpossibleMove


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

        pawn = board.squares['e2']
        board.move('e2', 'e3')
        self.assertIs(pawn, board.squares['e3'])
        self.assertIsNone(board.squares['e2'])

    def test_impossible_move(self):
        board = Board()
        self.assertRaises(ImpossibleMove, board.move, 'g1', 'g3')
        self.assertRaises(ImpossibleMove, board.move, 'b2', 'b5')

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

    def test_castling(self):
        board = Board(initial_pieces={'e1': King('white'), 'h1': Rook('white')})
        king = board.squares['e1']
        rook = board.squares['h1']
        board.move('e1', 'g1')
        self.assertIs(king, board.squares['g1'])
        self.assertIs(rook, board.squares['f1'])
        self.assertIsNone(board.squares['e1'])
        self.assertIsNone(board.squares['h1'])

    def test_fail_castling_when_rook_already_moved(self):
        board = Board(initial_pieces={'e1': King('white'), 'h1': Rook('white')})
        board.move('h1', 'h8')
        board.move('h8', 'h1')
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g1')

    def test_fail_castling_when_king_already_moved(self):
        board = Board(initial_pieces={'e1': King('white'), 'h1': Rook('white')})
        board.move('e1', 'f1')
        board.move('f1', 'e1')
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g1')

    def test_fail_castling_when_no_rook_involved(self):
        board = Board(initial_pieces={'e1': King('white'), 'h1': Queen('white')})
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g1')

    def test_fail_castling_when_is_not_same_line(self):
        board = Board(initial_pieces={'e1': King('white'), 'h1': Rook('white')})
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g2')

    def test_fail_castling_when_destiny_is_too_far(self):
        board = Board(initial_pieces={'e1': King('white'), 'h1': Rook('white')})
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'b1')

    def test_fail_castling_when_some_piece_is_between_king_rook(self):
        board = Board(initial_pieces={'e1': King('white'), 'f1': Queen('white'), 'h1': Rook('white')})
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'b1')

    def test_fail_castling_when_pieces_are_black_and_white(self):
        board = Board(initial_pieces={'e1': King('white'), 'h1': Rook('black')})
        self.assertRaises(ImpossibleMove, board.move, 'e1', 'g1')
