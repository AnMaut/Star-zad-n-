import pytest
from midterm_A import vyber_leku


@pytest.mark.parametrize(
    ("dna", "time", "expected_cure"),
    [
        ("MTZAMTAMTA", 9, "jablko"),
        ("MMMMMT", 5, "prasky"),
        ("MMMMMT", 3, "prasky"),
        ("AATTAATTAATTAATT", 3, "prasky"),
        ("AATTAATTAZZTTTTTTTT", 3, "injekce"),
        ("MZZZZ", 3, "prasky"),
    ]
)
def test_vyber_leku(dna, time, expected_cure):
    assert vyber_leku(dna, time) == expected_cure
