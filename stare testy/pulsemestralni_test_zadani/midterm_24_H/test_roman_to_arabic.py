import pytest

from midterm_H import roman_to_arabic


@pytest.mark.parametrize(
    ("roman_number", "expected_number"),
    [
        ("I", 1),
        ("III", 3),
        ("IV", 4),
        ("MMMMXC", 4090),
        ("CMXCIX", 999),
        ("CD", 400),
        ("DCCC", 800),
        ("CM", 900),
        ("MMMMM", 5000)
    ]
)
def test_roman_validator(roman_number, expected_number):
    number = roman_to_arabic(roman_number)
    assert number == expected_number
