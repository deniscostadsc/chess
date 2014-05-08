import pytest

from chess.board import Board, ImpossibleMove


def test_knight_can_moves():
    board = Board()
    knight = board.squares['b1']
    board.move('b1', 'c3')
    assert board.squares['c3'] is knight
    assert board.squares['b1'] is None


def test_knight_cant_moves():
    board = Board()
    with pytest.raises(ImpossibleMove):
        board.move('b1', 'c4')
