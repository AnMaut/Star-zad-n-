import pytest
from midterm_C import create_enemy
from midterm_C import DIFFICULTY_LEVEL


@pytest.mark.parametrize(
    ('selected_enemy', 'expected_enemy', 'expected_attack', 'expected_life'),
    [
        ('orc', 'orc', 3 * DIFFICULTY_LEVEL, 5 * DIFFICULTY_LEVEL),
        ('spider', 'spider', 2 * DIFFICULTY_LEVEL, DIFFICULTY_LEVEL),
        ('bat', 'bat', DIFFICULTY_LEVEL, 2 * DIFFICULTY_LEVEL)
    ]
)
def test_create_enemy(selected_enemy, expected_enemy, expected_attack, expected_life):
    enemy = create_enemy(selected_enemy)
    assert isinstance(enemy, dict) is True
    assert enemy['enemy_type'] == expected_enemy
    assert enemy['attack'] == expected_attack
    assert enemy['life'] == expected_life
