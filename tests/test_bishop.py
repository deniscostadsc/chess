import pytest

from chess.board import Board, ImpossibleMove
from chess.pieces import Bishop


def test_bishop_can_moves():
    bishop = Bishop('White')
    board = Board(initial_pieces={'f1': bishop})
    board.move('f1', 'h3')
    assert board.squares['h3'] is bishop
    assert board.squares['f1'] is None


def test_bishop_cant_moves():
    board = Board(initial_pieces={'f1': Bishop('White')})
    with pytest.raises(ImpossibleMove):
        board.move('f1', 'f3')
