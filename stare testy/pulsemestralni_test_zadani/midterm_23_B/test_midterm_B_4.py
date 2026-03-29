import pytest

from midterm_B import polybiuv_ctverec_desifrovani


@pytest.mark.parametrize(
    ("encoded_message", "expected_decoded_message"),
    [([42, 21, 13, 52, 35, 52, 0, 11, 45, 12, 33, 45, 23, 42, 12, 53, 23, 43, 21], "miluju programovani"),
     ([11, 14, 51, 34, 12, 43], "python"),
     ([52, 55, 0, 51, 21, 0, 51, 12, 32, 52, 43, 33, 52, 35, 31], "uz ti to funguje"),
    ]
)
def test_assignment(encoded_message, expected_decoded_message):
    assert polybiuv_ctverec_desifrovani(encoded_message) == expected_decoded_message
