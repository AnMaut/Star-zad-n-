import pytest
from midterm_C import generate_map


@pytest.mark.parametrize(
    ('input_tuple', 'expected_length'),
    [
        ((5, 3, 1, 1, 1, 7), 19),
        ((2, 7, 2, 1, 1, 3), 17),
        ((1, 1, 1, 1, 1, 1), 7),
        ((1, 2, 3, 4, 5, 6), 22),
        ((1, 2, 0, 0, 0, 6), 10)
    ]
)
def test_generate_map(input_tuple, expected_length):
    actual_map = generate_map(input_tuple)
    assert len(actual_map) == expected_length
    assert isinstance(actual_map, list) is True
    assert all(i for i in actual_map if i is str) is True
    assert actual_map[-1] == 'finish'
