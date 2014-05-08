import pytest

from chess.pieces import Bishop, InvalidChessColor


def test_can_instantiate_with_different_cases():
    assert isinstance(Bishop('WhItE'), Bishop)
    assert isinstance(Bishop('wHiTe'), Bishop)


def test_pieces_cant_be_instatiated_with_invalid_color():
    with pytest.raises(InvalidChessColor):
        Bishop('blue')


def test_pieces_should_have_correct_color():
    assert Bishop('black').color == 'black'
    assert Bishop('white').color == 'white'


def test_pieces_should_have_correct_name():
    assert Bishop('white').name == 'White Bishop'
