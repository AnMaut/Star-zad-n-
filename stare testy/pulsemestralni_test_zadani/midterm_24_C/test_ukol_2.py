import pytest
from midterm_C import create_hero


@pytest.mark.parametrize(
    ('selected_class', 'selected_name', 'expected_class', 'expected_name', 'expected_attack'),
    [
        ('warrior', 'Rozbijec', 'warrior', 'Rozbijec', 6),
        ('ranger', 'Propichovac', 'ranger', 'Propichovac', 5),
        ('wizard', 'Bleskonos', 'wizard', 'Bleskonos', 3),
    ]
)
def test_create_hero(selected_class, selected_name, expected_class, expected_name, expected_attack):
    hero = create_hero(selected_class, selected_name)
    assert isinstance(hero, dict) is True
    assert hero['class'] == expected_class
    assert hero['name'] == expected_name
    assert hero['attack'] == expected_attack
