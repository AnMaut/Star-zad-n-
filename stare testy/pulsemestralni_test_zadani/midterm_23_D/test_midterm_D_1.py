import pytest

from midterm_D_sol import get_attack_stats
from midterm_D_sol import FAST_ATTACK_NAMES, FAST_ATTACK_STATS, CHARGED_ATTACK_NAMES, CHARGED_ATTACK_STATS


@pytest.mark.parametrize(
    ("name", "attack_name", "attacks_names", "attacks_stats", "expected_stats"),
    [
        ("Bulbasaur", "Tackle", FAST_ATTACK_NAMES, FAST_ATTACK_STATS, (5, 5, 0.5)),
        ("Bulbasaur", "Sludge Bomb", CHARGED_ATTACK_NAMES, CHARGED_ATTACK_STATS, (80, 50, 2.3)),
        ("Charmander", "Scratch", FAST_ATTACK_NAMES, FAST_ATTACK_STATS, (6, 4, 0.5)),
        ("Charmander", "Flamethrower", CHARGED_ATTACK_NAMES, CHARGED_ATTACK_STATS, (70, 50, 2.2)),
        ("Squirtle", "Tackle", FAST_ATTACK_NAMES, FAST_ATTACK_STATS, (5, 5, 0.5)),
        ("Squirtle", "Water Pulse", CHARGED_ATTACK_NAMES, CHARGED_ATTACK_STATS, (70, 50, 3.2))
    ]
)
def test_get_attack_stats(name, attack_name, attacks_names, attacks_stats, expected_stats):
    assert get_attack_stats(name, attack_name, attacks_names, attacks_stats) == expected_stats
