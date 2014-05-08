import pytest

from chess.board import Board, ImpossibleMove
from chess.pieces import Rook


def test_rook_can_moves():
    rook = Rook('white')
    board = Board(initial_pieces={'d5': rook})
    board.move('d5', 'd8')
    assert board.get_piece('d8') is rook
    assert board.get_piece('d5') is None


def test_rook_cant_moves():
    board = Board(initial_pieces={'e5': Rook('white')})
    with pytest.raises(ImpossibleMove):
        board.move('e5', 'd8')
