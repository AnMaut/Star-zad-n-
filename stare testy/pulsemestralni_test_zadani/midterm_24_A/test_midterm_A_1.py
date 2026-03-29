import pytest
from midterm_A import geneticka_predispozice_lecby


@pytest.mark.parametrize(
    ("dna", "expected_time"),
    [
        ("MTZAMTAMTA", 9),
        ("MMMMMT", 3),
        ("ZMZMZMZMZMZMZMZMZMZMZMZM", 3),
        ("AATTAATTAATTAATT", 9),
        ("AATTAATTAZZTTTTTTTT", 3)
    ]
)
def test_geneticka_predispozice_lecby(dna, expected_time):
    assert geneticka_predispozice_lecby(dna) == expected_time
