import pytest

from midterm_D_sol import get_best_attacks


@pytest.mark.parametrize(
    ("name", "fast_attacks", "charged_attacks", "expected_dps", "expected_best_fast", "expected_best_charged"),
    [
        ("Bulbasaur", ["Vine Whip", "Tackle"], ["Seed Bomb", "Sludge Bomb", "Power Whip"], 19.47, "Vine Whip", "Power Whip"),
        ("Charmander", ["Ember", "Scratch"], ["Flamethrower", "Flame Charge", "Flame Burst"], 17.4, "Scratch", "Flamethrower"),
        ("Squirtle", ["Tackle", "Bubble"], ["Aqua Jet", "Aqua Tail", "Water Pulse"], 16.62, "Bubble", "Aqua Tail"),
    ]
)
def test_get_best_attacks(name, fast_attacks, charged_attacks, expected_dps, expected_best_fast, expected_best_charged):
    dps, fast, charged = get_best_attacks(name, fast_attacks, charged_attacks)
    assert dps == expected_dps
    assert fast == expected_best_fast
    assert charged == expected_best_charged
