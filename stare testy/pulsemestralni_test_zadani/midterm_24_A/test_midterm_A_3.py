import pytest
from midterm_A import samovolna_mutace


@pytest.mark.parametrize(
    ("dna", "cure", "expected_mutation"),
    [
        ("MTZAMTAMTA", "prasky", "Pokemon se vyvinul na jeho dalsi level"),
        ("MTZAMTAMTA", "injekce", "Pokemon se vyvinul na jeho dalsi level"),
        ("MTZAMTAMTA", "jablko", "Pokemon se uzdravil bez mutace"),
        ("ZZZZZZ", "prasky", "Pokemon se uzdravil, ale nema dostatecnou energii se vyvinout"),
        ("AATTAATTA", "injekce", "Pokemon se vyvinul na jeho dalsi level"),
        ("AATZAAZAA", "injekce", "Pokemon se uzdravil, ale nema dostatecnou energii se vyvinout"),
    ]
)
def test_samovolna_mutace(dna, cure, expected_mutation):
    assert samovolna_mutace(dna, cure) == expected_mutation
