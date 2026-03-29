import pytest

from midterm_H import sort_and_convert


@pytest.mark.parametrize(
    ("numbers", "expected_romans", "expected_arabics"),
    [
        ([1, 2, 4, 10], ["I", "II", "IV", "X"], []),
        (["I", "II", "IV", "X"], [], [1, 2, 4, 10]),
        (["III", 3, 4, 15, 68, "CCCC", "DCCC", 1024, "XL"], ['III', "IV", 'XV', 'LXVIII', 'MXXIV'], [3, 400, 800, 40]),
    ]
)
def test_roman_validator(numbers, expected_romans, expected_arabics):
    romans, arabics = sort_and_convert(numbers)
    assert romans == expected_romans
    assert arabics == expected_arabics
