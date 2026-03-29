import pytest

from midterm_E import molecular_weight


@pytest.mark.parametrize(
    ('molecule', 'expected_weight'),
    [
        (['H2O'], ['5.7 mol']),
        (['He2O'], ['5.5 mol']),
        (['He'], ['2 mol']),
        (['FeHe'], ['3.6 mol']),
    ]
)
def test_assignment(molecule, expected_weight):
    assert molecular_weight(molecule) == expected_weight
