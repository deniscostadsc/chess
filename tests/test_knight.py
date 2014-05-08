import pytest

from chess.board import Board, ImpossibleMove


def test_knight_can_moves():
    board = Board()
    knight = board.get_piece('b1')
    board.move('b1', 'c3')
    assert board.get_piece('c3') is knight
    assert board.get_piece('b1') is None


def test_knight_cant_moves():
    board = Board()
    with pytest.raises(ImpossibleMove):
        board.move('b1', 'c4')
