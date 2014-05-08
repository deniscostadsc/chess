import pytest

from chess.board import Board, ImpossibleMove
from chess.pieces import Pawn


def test_pawn_can_moves():
    board = Board()
    pawn = board.get_piece('e2')
    board.move('e2', 'e3')
    assert board.get_piece('e3') is pawn
    assert board.get_piece('e2') is None


def test_pawn_can_moves_two_squares():
    board = Board()
    pawn = board.get_piece('e2')
    board.move('e2', 'e4')
    assert board.get_piece('e4') is pawn
    assert board.get_piece('e2') is None


def test_pawn_cant_moves_two_squares_after_moved():
    board = Board()
    board.move('e2', 'e3')
    with pytest.raises(ImpossibleMove):
        board.move('e3', 'f5')


def test_pawn_cant_move_back():
    board = Board(initial_pieces={'b4': Pawn('white')})
    with pytest.raises(ImpossibleMove):
        assert board.move('b4', 'b3')


def test_pawn_cant_move_diagonally():
    board = Board()
    with pytest.raises(ImpossibleMove):
        board.move('e2', 'f3')
