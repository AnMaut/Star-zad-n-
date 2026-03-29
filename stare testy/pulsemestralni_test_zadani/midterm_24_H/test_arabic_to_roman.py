import pytest

from midterm_H import arabic_to_roman


@pytest.mark.parametrize(
    ("arabic_number", "expected_number"),
    [
        (1, "I"),
        (3, "III"),
        (4, "IV"),
        (4090, "MMMMXC"),
        (999, "CMXCIX"),
        (400, "CD"),
        (800, "DCCC"),
        (900, "CM"),
        (5000, "MMMMM")
    ]
)
def test_roman_validator(arabic_number, expected_number):
    number = arabic_to_roman(arabic_number)
    assert number == expected_number
