import pytest

from chess.board import Board, ImpossibleMove
from chess.pieces import King, Rook, Pawn, Knight


def test_board_has_32_pieces():
    board = Board()
    assert board.pieces_quantity() == 32


def test_board_can_be_instatiated_with_any_set_of_pieces():
    board = Board(initial_pieces={'a2': Pawn('white'), 'a6': Pawn('black')})
    assert board.pieces_quantity() == 2


def test_piece_cant_capture_an_ally():
    board = Board(initial_pieces={'e5': Pawn('white'), 'f3': Knight('white')})
    with pytest.raises(ImpossibleMove):
        board.move('f3', 'e5')


def test_alternating_between_players():
    board = Board()
    assert board.turn == 'white'
    board.move('g2', 'g3')  # white pawn moves
    assert board.turn == 'black'
    board.move('b7', 'b6')  # black pawn moves
    assert board.turn == 'white'
    board.move('f1', 'g2')  # white bishop moves
    assert board.turn == 'black'


def test_only_white_pieces_can_start():
    board = Board()
    assert board.turn == 'white'
    with pytest.raises(ImpossibleMove):
        board.move('b7', 'b6')


def test_players_can_put_opponent_in_check():
    board = Board({'e1': King('black'), 'f8': Rook('white')})
    assert board.check is None
    board.move('f8', 'e8')
    assert board.check == 'black'


def test_players_can_get_out_of_check():
    board = Board({'e1': King('black'), 'f8': Rook('white'), 'a1': King('white')})
    assert board.check is None
    board.move('f8', 'e8')
    assert board.check == 'black'
    board.move('e1', 'f1')
    assert board.check is None


def test_player_should_to_get_out_of_check():
    board = Board({'e1': King('black'), 'f8': Rook('white'), 'a1': King('white')})
    assert board.check is None
    board.move('f8', 'e8')
    assert board.check == 'black'
    with pytest.raises(ImpossibleMove):
        board.move('e1', 'e2')


def test_pieces_can_capture_opponent_pieces():
    board = Board(initial_pieces={'a8': King('black'), 'e5': Pawn('black'), 'f3': Knight('white')})
    assert board.pieces_quantity() == 3

    knight = board.get_piece('f3')
    board.move('f3', 'e5')
    assert board.get_piece('e5') is knight
    assert board.pieces_quantity() == 2
