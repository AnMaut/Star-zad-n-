import pytest
from midterm_C import resolve_fight
from midterm_C import DIFFICULTY_LEVEL


@pytest.mark.parametrize(
    ('enemy', 'hero', 'expected_winner', 'hero_won'),
    [
        ({'enemy_type': 'orc', 'attack': 3 * DIFFICULTY_LEVEL, 'life': 5 * DIFFICULTY_LEVEL},
         {'name': 'Stahovac', 'class': 'ranger', 'attack': 5, 'food': 5, 'life': 4.0, 'maximum_life': 4.0, 'gold': 0},
         {'enemy_type': 'orc', 'attack': 2.25, 'life': 1.5}, False),
        ({'enemy_type': 'spider', 'attack': 2 * DIFFICULTY_LEVEL, 'life': 1 * DIFFICULTY_LEVEL},
         {'name': 'Stahovac', 'class': 'ranger', 'attack': 5, 'food': 5, 'life': 4.0, 'maximum_life': 4.0, 'gold': 0},
         {'name': 'Stahovac', 'class': 'ranger', 'attack': 4, 'food': 4, 'life': 2.5, 'maximum_life': 4.0, 'gold': 0},
         True),
        ({'enemy_type': 'bat', 'attack': 1 * DIFFICULTY_LEVEL, 'life': 2 * DIFFICULTY_LEVEL},
         {'name': 'Ohnosleh', 'class': 'wizard', 'attack': 3, 'food': 0, 'life': 3.0, 'maximum_life': 3.0, 'gold': 5},
         {'name': 'Ohnosleh', 'class': 'wizard', 'attack': 1, 'food': 0, 'life': 0.75, 'maximum_life': 3.0, 'gold': 5},
         True)
    ]
)
def test_resolve_fight(enemy, hero, expected_winner, hero_won):
    winner, won = resolve_fight(enemy, hero)
    assert isinstance(winner, dict) is True
    assert isinstance(won, bool) is True
    assert winner == expected_winner
    assert won == hero_won
