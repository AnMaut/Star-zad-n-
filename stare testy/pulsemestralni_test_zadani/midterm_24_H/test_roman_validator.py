import pytest

from midterm_H import roman_validator


@pytest.mark.parametrize(
    ("number", "expected_is_roman", "expected_correct_number"),
    [
        ("IIII", True, "IV"),
        ("MMMMLXXXX", True, "MMMMXC"),
        (1024, False, None),
        ("DCCCCLXXXXVIIII", True, "CMXCIX"),
        ("CCCC", True, "CD"),
        ("DCCC", True, "DCCC"),
        ("DCCCC", True, "CM"),
        ("MMMMM", True, "MMMMM"),
    ]
)
def test_roman_validator(number, expected_is_roman, expected_correct_number):
    is_roman, correct_number = roman_validator(number)
    assert is_roman == expected_is_roman
    assert correct_number == expected_correct_number
