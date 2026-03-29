import pytest

from midterm_D_sol import get_dps


@pytest.mark.parametrize(
    ("name", "fast_attack", "charged_attack", "simulation_time", "expected_attacks", "expected_dps"),
    [
        ("Bulbasaur", "Tackle", "Power Whip", 15,
         ['Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle',
          'Power Whip', 'Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle', 'Tackle',
          'Tackle', 'Power Whip'], 19),
        ("Bulbasaur", "Vine Whip", "Sludge Bomb", 15,
         ['Vine Whip', 'Vine Whip', 'Vine Whip', 'Vine Whip', 'Vine Whip', 'Vine Whip', 'Vine Whip', 'Vine Whip',
          'Vine Whip', 'Sludge Bomb', 'Vine Whip', 'Vine Whip', 'Vine Whip', 'Vine Whip', 'Vine Whip', 'Vine Whip',
          'Vine Whip', 'Vine Whip', 'Sludge Bomb', 'Vine Whip'], 19),
        ("Charmander", "Scratch", "Flame Charge", 15,
         ['Scratch', 'Scratch', 'Scratch', 'Scratch', 'Scratch', 'Scratch', 'Scratch', 'Scratch', 'Scratch',
          'Flame Charge', 'Scratch', 'Scratch', 'Scratch', 'Scratch', 'Scratch', 'Scratch', 'Scratch', 'Scratch',
          'Flame Charge'], 16),
        ("Charmander", "Ember", "Flamethrower", 150, [], 17),
        ("Squirtle", "Tackle", "Aqua Tail", 200, [], 17),
        ("Squirtle", "Tackle", "Water Pulse", 120, [], 16)
    ]
)
def test_get_attack_stats(name, fast_attack, charged_attack, simulation_time, expected_attacks, expected_dps):
    attacks, dps = get_dps(name, fast_attack, charged_attack, 15)
    print(attacks)
    if simulation_time < 20:
        assert attacks == expected_attacks
    assert round(dps) == expected_dps


@pytest.mark.parametrize(
    ("name", "fast_attack", "charged_attack", "expected_dps"),
    [
        ("Squirtle", "Tackle", "Water Pulse", 14.6)
    ]
)
def test_get_attack_stats2(name, fast_attack, charged_attack, expected_dps):
    attacks, dps = get_dps(name, fast_attack, charged_attack)
    assert dps == expected_dps
