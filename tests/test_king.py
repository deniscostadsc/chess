import pytest

from chess.board import Board, ImpossibleMove
from chess.pieces import King, Rook, Pawn, Queen


def test_king_can_moves():
    king = King('white')
    #
    # I have to pass a second king because the board look for a second
    # king when you set the first one. Maybe a have to add an attribute
    # to the board class to say wether the match is tutorial or not.
    #
    board = Board(initial_pieces={'f5': king, 'h1': King('black')})
    board.move('f5', 'e5')
    assert board.squares['e5'] is king
    assert board.squares['f5'] is None


def test_king_cant_moves():
    board = Board(initial_pieces={'a1': King('white'), 'h1': King('black')})
    with pytest.raises(ImpossibleMove):
        board.move('a1', 'a3')


def test_king_can_do_castling_to_right():
    board = Board(initial_pieces={'e1': King('white'), 'h1': Rook('white')})
    king = board.squares['e1']
    rook = board.squares['h1']
    board.move('e1', 'g1')
    assert board.squares['g1'] == king
    assert board.squares['f1'] == rook
    assert board.squares['e1'] is None
    assert board.squares['h1'] is None


def test_king_can_do_castling_to_left():
    board = Board(initial_pieces={'e1': King('white'), 'a1': Rook('white')})
    king = board.squares['e1']
    rook = board.squares['a1']
    board.move('e1', 'c1')
    assert board.squares['c1'] == king
    assert board.squares['d1'] == rook
    assert board.squares['e1'] is None
    assert board.squares['a1'] is None


def test_king_cant_do_castling_when_rook_already_moved():
    board = Board(initial_pieces={
        'a8': King('black'),
        'a7': Pawn('black'),
        'e1': King('white'),
        'h1': Rook('white')
    })
    board.move('h1', 'h7')  # rook moves
    board.move('a7', 'a6')  # black pawn moves
    board.move('h7', 'h1')  # rook moves back
    board.move('a6', 'a5')  # black pawn moves again
    with pytest.raises(ImpossibleMove):
        board.move('e1', 'g1')


def test_fail_castling_when_king_already_moved():
    board = Board(initial_pieces={
        'a8': King('black'),
        'a7': Pawn('black'),
        'e1': King('white'),
        'h1': Rook('white')})
    board.move('e1', 'f1')  # king moves
    board.move('a7', 'a6')  # pawn moves
    board.move('f1', 'e1')  # king moves back
    board.move('a6', 'a5')  # pawn moves again
    with pytest.raises(ImpossibleMove):
        board.move('e1', 'g1')


def test_king_cant_do_castling_with_a_rook_of_a_different_color():
    board = Board(initial_pieces={'e1': King('white'), 'h1': Rook('black')})
    with pytest.raises(ImpossibleMove):
        board.move('e1', 'g1')


def test_king_cant_do_castlig_with_there_is_a_pieces_between_king_and_rook():
    board = Board(initial_pieces={'e1': King('white'), 'f1': Queen('white'), 'h1': Rook('white')})
    with pytest.raises(ImpossibleMove):
        board.move('e1', 'g1')


def test_king_cant_do_castling_when_rook_is_not_same_line():
    board = Board(initial_pieces={'e1': King('white'), 'h2': Rook('white')})
    with pytest.raises(ImpossibleMove):
        board.move('e1', 'g2')


def test_king_cant_do_castling_when_destiny_is_too_far():
    board = Board(initial_pieces={'e1': King('white'), 'a1': Rook('white')})
    with pytest.raises(ImpossibleMove):
        board.move('e1', 'b1')


def test_king_cant_do_castling_when_no_rook_is_involved():
    board = Board(initial_pieces={'e1': King('white'), 'h1': Queen('white')})
    with pytest.raises(ImpossibleMove):
        board.move('e1', 'g1')


def test_king_cant_do_castling_when_pieces_start_in_wrong_place():
    board = Board(initial_pieces={'e2': King('white'), 'h2': Rook('black')})
    with pytest.raises(ImpossibleMove):
        board.move('e2', 'g2')
