import pytest

from midterm_E import synthesis


@pytest.mark.parametrize(
    ('molecules', 'expected_molecule'),
    [
        (['2He', 'O', 'O'], ['He22O']),
        (['H', 'O'], ['HO']),
        (['HO'], 'synteza neni mozna'),
        (['Fe', 'H'], ['FeH']),
        (['RCHOO', 'O'], ['RCH3O']),
        ([], 'synteza neni mozna'),
    ]
)
def test_synthesis(molecules, expected_molecule):
    assert synthesis(molecules) == expected_molecule
