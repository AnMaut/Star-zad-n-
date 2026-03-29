import pytest
from midterm_C import resolve_room


@pytest.mark.parametrize(
    ('room', 'hero', 'expected_hero'),
    [
        ('empty room',
         {'name': 'Stahovac', 'class': 'ranger', 'attack': 5, 'food': 5, 'life': 4.0, 'maximum_life': 4.0, 'gold': 0},
         {'name': 'Stahovac', 'class': 'ranger', 'attack': 5, 'food': 6, 'life': 4.0, 'maximum_life': 4.0, 'gold': 0}),
        ('empty room',
         {'name': 'Bleskous', 'class': 'wizard', 'attack': 5, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 0},
         {'name': 'Bleskous', 'class': 'wizard', 'attack': 8, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 0}),
        ('empty room',
         {'name': 'Bleskous', 'class': 'wizard', 'attack': 2, 'food': 0, 'life': 2.0, 'maximum_life': 3.0, 'gold': 0},
         {'name': 'Bleskous', 'class': 'wizard', 'attack': 5, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 0}),
        ('armory',
         {'name': 'Stahovac', 'class': 'ranger', 'attack': 5, 'food': 5, 'life': 4.0, 'maximum_life': 4.0, 'gold': 0},
         {'name': 'Stahovac', 'class': 'ranger', 'attack': 6, 'food': 5, 'life': 4.0, 'maximum_life': 4.0, 'gold': 0}),
        ('armory',
         {'name': 'Brutous', 'class': 'warrior', 'attack': 5, 'food': 0, 'life': 4.0, 'maximum_life': 5.0, 'gold': 0},
         {'name': 'Brutous', 'class': 'warrior', 'attack': 7, 'food': 0, 'life': 4.0, 'maximum_life': 5.0, 'gold': 0}),
        ('armory',
         {'name': 'Bleskous', 'class': 'wizard', 'attack': 2, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 0},
         {'name': 'Bleskous', 'class': 'wizard', 'attack': 2, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 0}),
        ('treasury',
         {'name': 'Bleskous', 'class': 'wizard', 'attack': 2, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 0},
         {'name': 'Bleskous', 'class': 'wizard', 'attack': 2, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 1}),
        ('orc',
         {'name': 'Bleskous', 'class': 'wizard', 'attack': 8, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 0},
         {'name': 'Bleskous', 'class': 'died', 'attack': 5, 'food': 0, 'life': -1.5, 'maximum_life': 3.0, 'gold': 0}),
        ('finish',
         {'name': 'Krutak', 'class': 'wizard', 'attack': 8, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 0},
         {'name': 'Krutak', 'class': 'winner', 'attack': 8, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 0}),
    ]
)
def test_resolve_room(room, hero, expected_hero):
    updated_hero = resolve_room(room, hero)
    assert isinstance(updated_hero, dict) is True
    assert updated_hero == expected_hero
