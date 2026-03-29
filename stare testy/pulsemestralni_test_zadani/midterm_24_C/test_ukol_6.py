import pytest
from midterm_C import run_adventure


@pytest.mark.parametrize(
    ('rooms', 'hero_class', 'hero_name', 'expected_end'),
    [
        ((5, 5, 0, 0, 0, 10), 'warrior', 'Krutoprisnak', True),
        ((1, 1, 10, 10, 10, 1), 'warrior', 'Troubasmolar', False),
        ((1, 1, 10, 10, 10, 1), 'warriorr', 'Nevimcojsem', False),
    ]
)
def test_run_adventure(rooms, hero_class, hero_name, expected_end):
    adventure_end = run_adventure(rooms, hero_class, hero_name)
    assert isinstance(adventure_end, bool) is True
    assert adventure_end == expected_end
