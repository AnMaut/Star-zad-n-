import pytest

from midterm_E import decomposition


@pytest.mark.parametrize(
    ('molecules', "expected_molecules"),
    [
        (['H2O'], ['H', 'O']),
        (['H2OOO'], ['H', 'O', 'O', 'O']),
        (['HO'], ['H', 'O']),
        (['Fe2H'], ['Fe', 'H']),
        (['Fe2H', 'H'], 'analyticka reakce neni mozna'),
        ([], 'analyticka reakce neni mozna'),
    ]
)
def test_decomposition(molecules, expected_molecules):
    assert decomposition(molecules) == expected_molecules
