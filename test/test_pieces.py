try:
    import unittest2 as unittest
except ImportError:
    import unittest

from chess.pieces import Bishop, King, Knight, Pawn, Queen, Rook, InvalidChessColor


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
        self.assertTrue(bishop.can_move('f1', 'g2'))
        self.assertTrue(bishop.can_move('f1', 'a6'))

    def test_fail_bishop_move(self):
        bishop = Bishop('white')
        self.assertFalse(bishop.can_move('f1', 'f2'))
        self.assertFalse(bishop.can_move('a1', 'a3'))


class TestRookMoves(unittest.TestCase):
    def test_rook_move(self):
        rook = Rook('white')
        self.assertTrue(rook.can_move('d5', 'd8'))
        self.assertTrue(rook.can_move('e2', 'h2'))

    def test_fail_rook_move(self):
        rook = Rook('white')
        self.assertFalse(rook.can_move('e5', 'd8'))
        self.assertFalse(rook.can_move('a1', 'h8'))


class TestKingMoves(unittest.TestCase):
    def test_king_move(self):
        king = King('white')
        self.assertTrue(king.can_move('f5', 'e5'))
        self.assertTrue(king.can_move('e5', 'f5'))

    def test_fail_king_move(self):
        king = King('white')
        self.assertFalse(king.can_move('a1', 'h8'))
        self.assertFalse(king.can_move('h1', 'a8'))


class TestQueenMoves(unittest.TestCase):
    def test_queen_move_as_rook(self):
        queen = Queen('white')
        self.assertTrue(queen.can_move('d5', 'd8'))
        self.assertTrue(queen.can_move('e2', 'h2'))

    def test_queen_move_as_bishop(self):
        queen = Queen('white')
        self.assertTrue(queen.can_move('f1', 'g2'))
        self.assertTrue(queen.can_move('f1', 'a6'))

    def test_fail_queen_move(self):
        queen = Queen('white')
        self.assertFalse(queen.can_move('a1', 'h7'))
        self.assertFalse(queen.can_move('d4', 'f5'))


class TestPawnMoves(unittest.TestCase):
    def test_pawn_move(self):
        pawn = Pawn('white')
        self.assertTrue(pawn.can_move('b4', 'b5'))
        self.assertTrue(pawn.can_move('e7', 'e8'))

    def test_fail_pawn_move(self):
        pawn = Pawn('white')
        self.assertFalse(pawn.can_move('e2', 'e8'))

    def test_fail_pawn_move_back(self):
        pawn = Pawn('white')
        self.assertFalse(pawn.can_move('b4', 'b3'))


class TestKnightMoves(unittest.TestCase):
    def test_knight_move(self):
        knight = Knight('white')
        self.assertTrue(knight.can_move('d4', 'b5'))
        self.assertTrue(knight.can_move('d4', 'c6'))
        self.assertTrue(knight.can_move('d4', 'e6'))
        self.assertTrue(knight.can_move('d4', 'f5'))
        self.assertTrue(knight.can_move('d4', 'b3'))
        self.assertTrue(knight.can_move('d4', 'c2'))
        self.assertTrue(knight.can_move('d4', 'e2'))
        self.assertTrue(knight.can_move('d4', 'f3'))

    def test_fail_knight_move(self):
        knight = Knight('white')
        self.assertFalse(knight.can_move('d4', 'd3'))
        self.assertFalse(knight.can_move('d4', 'b2'))
        self.assertFalse(knight.can_move('d4', 'd1'))
        self.assertFalse(knight.can_move('d4', 'h8'))


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
