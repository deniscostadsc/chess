import pytest

from chess.board import Board, ImpossibleMove
from chess.pieces import Queen


def test_queen_can_moves_as_rook():
    queen = Queen('white')
    board = Board(initial_pieces={'d5': queen})
    board.move('d5', 'd8')
    assert board.get_piece('d8') is queen
    assert board.get_piece('d5') is None


def test_queen_can_moves_as_bishop():
    queen = Queen('white')
    board = Board(initial_pieces={'f1': queen})
    board.move('f1', 'g2')
    assert board.get_piece('g2') is queen
    assert board.get_piece('f1') is None


def test_cant_moves():
    board = Board(initial_pieces={'a1': Queen('white')})
    with pytest.raises(ImpossibleMove):
        board.move('a1', 'h7')
