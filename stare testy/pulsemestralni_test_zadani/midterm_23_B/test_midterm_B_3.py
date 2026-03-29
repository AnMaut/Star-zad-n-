import pytest

from midterm_B import polybiuv_ctverec_sifrovani


@pytest.mark.parametrize(
    ("message", "expected_encoded_message"),
    [("Miluju programovani", [42, 21, 13, 52, 35, 52, 0, 11, 45, 12, 33, 45, 23, 42, 12, 53, 23, 43, 21]),
     ("Python", [11, 14, 51, 34, 12, 43]),
     ("Uz Ti to funguje", [52, 55, 0, 51, 21, 0, 51, 12, 32, 52, 43, 33, 52, 35, 31]),
    ]
)
def test_assignment(message, expected_encoded_message):
    assert polybiuv_ctverec_sifrovani(message) == expected_encoded_message
