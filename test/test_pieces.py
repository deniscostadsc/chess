try:
    import unittest2 as unittest
except ImportError:
    import unittest

from chess.pieces import (
    Bishop, King, Knight, Pawn, Queen, Rook,
    ImpossibleMove, InvalidChessColor
)


class TestInstantiationPieces(unittest.TestCase):
    def test_raises_exception_on_unknown_color(self):
        self.assertRaises(InvalidChessColor, Bishop, 'blue')

    def test_instantiate_with_different_cases(self):
        self.assertIsInstance(Bishop('WhItE'), Bishop)
        self.assertIsInstance(Bishop('wHiTe'), Bishop)
        self.assertIsInstance(Bishop('White'), Bishop)


class TestColorPieces(unittest.TestCase):
    def test_bishop_is_black(self):
        bishop = Bishop('black')
        self.assertEqual('black', bishop.color)

    def test_bishop_is_white(self):
        bishop = Bishop('white')
        self.assertEqual('white', bishop.color)

    def test_rook_is_black(self):
        rook = Rook('black')
        self.assertEqual('black', rook.color)

    def test_rook_is_white(self):
        rook = Rook('white')
        self.assertEqual('white', rook.color)

    def test_king_is_black(self):
        king = King('black')
        self.assertEqual('black', king.color)

    def test_king_is_white(self):
        king = King('white')
        self.assertEqual('white', king.color)

    def test_queen_is_black(self):
        queen = Queen('black')
        self.assertEqual('black', queen.color)

    def test_queen_is_white(self):
        queen = Queen('white')
        self.assertEqual('white', queen.color)

    def test_pawn_is_black(self):
        pawn = Pawn('black')
        self.assertEqual('black', pawn.color)

    def test_pawn_is_white(self):
        pawn = Pawn('white')
        self.assertEqual('white', pawn.color)

    def test_knight_is_black(self):
        knight = Knight('black')
        self.assertEqual('black', knight.color)

    def test_knight_is_white(self):
        knight = Knight('white')
        self.assertEqual('white', knight.color)


class TestBishopMoves(unittest.TestCase):
    def test_bishop_move(self):
        bishop = Bishop('white')
        self.assertEqual('g2', bishop.move('f1', 'g2'))
        self.assertEqual('a6', bishop.move('f1', 'a6'))

    def test_fail_bishop_move(self):
        bishop = Bishop('white')
        self.assertRaises(ImpossibleMove, bishop.move, 'f1', 'f2')
        self.assertRaises(ImpossibleMove, bishop.move, 'a1', 'a3')


class TestRookMoves(unittest.TestCase):
    def test_rook_move(self):
        rook = Rook('white')
        self.assertEqual('d8', rook.move('d5', 'd8'))
        self.assertEqual('h2', rook.move('e2', 'h2'))

    def test_fail_rook_move(self):
        rook = Rook('white')
        self.assertRaises(ImpossibleMove, rook.move, 'e5', 'd8')
        self.assertRaises(ImpossibleMove, rook.move, 'a1', 'h8')


class TestKingMoves(unittest.TestCase):
    def test_king_move(self):
        king = King('white')
        self.assertEqual('e5', king.move('f5', 'e5'))
        self.assertEqual('f5', king.move('e5', 'f5'))

    def test_fail_king_move(self):
        king = King('white')
        self.assertRaises(ImpossibleMove, king.move, 'a1', 'h8')
        self.assertRaises(ImpossibleMove, king.move, 'h1', 'a8')


class TestQueenMoves(unittest.TestCase):
    def test_queen_move_as_rook(self):
        queen = Queen('white')
        self.assertEqual('d8', queen.move('d5', 'd8'))
        self.assertEqual('h2', queen.move('e2', 'h2'))

    def test_queen_move_as_bishop(self):
        queen = Queen('white')
        self.assertEqual('g2', queen.move('f1', 'g2'))
        self.assertEqual('a6', queen.move('f1', 'a6'))

    def test_fail_queen_move(self):
        queen = Queen('white')
        self.assertRaises(ImpossibleMove, queen.move, 'a1', 'h7')
        self.assertRaises(ImpossibleMove, queen.move, 'd4', 'f5')


class TestPawnMoves(unittest.TestCase):
    def test_pawn_move(self):
        pawn = Pawn('white')
        self.assertEqual('b5', pawn.move('b4', 'b5'))
        self.assertEqual('e8', pawn.move('e7', 'e8'))

    def test_fail_pawn_move(self):
        pawn = Pawn('white')
        self.assertRaises(ImpossibleMove, pawn.move, 'e2', 'e8')


class TestKnightMoves(unittest.TestCase):
    def test_knight_move(self):
        knight = Knight('white')
        self.assertEqual('b5', knight.move('d4', 'b5'))
        self.assertEqual('c6', knight.move('d4', 'c6'))
        self.assertEqual('e6', knight.move('d4', 'e6'))
        self.assertEqual('f5', knight.move('d4', 'f5'))
        self.assertEqual('b3', knight.move('d4', 'b3'))
        self.assertEqual('c2', knight.move('d4', 'c2'))
        self.assertEqual('e2', knight.move('d4', 'e2'))
        self.assertEqual('f3', knight.move('d4', 'f3'))

    def test_fail_knight_move(self):
        knight = Knight('white')
        self.assertRaises(ImpossibleMove, knight.move, 'd4', 'd3')
        self.assertRaises(ImpossibleMove, knight.move, 'd4', 'b2')
        self.assertRaises(ImpossibleMove, knight.move, 'd4', 'd1')
        self.assertRaises(ImpossibleMove, knight.move, 'd4', 'h8')


class TestStrPieces(unittest.TestCase):
    def test_pawn_name(self):
        pawn = Pawn('white')
        self.assertEqual('Pawn', pawn.name)

    def test_rook_name(self):
        rook = Rook('white')
        self.assertEqual('Rook', rook.name)

    def test_knight_name(self):
        knight = Knight('white')
        self.assertEqual('Knight', knight.name)

    def test_bishop_name(self):
        bishop = Bishop('white')
        self.assertEqual('Bishop', bishop.name)

    def test_queen_name(self):
        queen = Queen('white')
        self.assertEqual('Queen', queen.name)

    def test_king_name(self):
        king = King('white')
        self.assertEqual('King', king.name)
