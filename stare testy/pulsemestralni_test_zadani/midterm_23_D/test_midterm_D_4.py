import pytest

from midterm_D_sol import main


@pytest.mark.parametrize(
    ("pokemons", "expected_pokemon_eval"),
    [
        (
            [
                ("Bulbasaur", "Vine Whip", "Sludge Bomb"),
                ("Bulbasaur", "Vine Whip", "Power Whip"),
            ],
            [
                ('Bulbasaur', 'Vine Whip', 'Power Whip', False, 0.879999999999999),
                ('Bulbasaur', 'Vine Whip', 'Power Whip', True, 0.0),
            ],
        ),
        (
            [
                ("Charmander", "Scratch", "Flame Burst"),
                ("Squirtle", "Bubble", "Water Pulse"),
                ("Squirtle", "Bubble", "Aqua Jet"),
            ],
            [
                ('Charmander', 'Scratch', 'Flamethrower', False, 1.1199999999999974),
                ('Squirtle', 'Bubble', 'Aqua Tail', False, 1.6400000000000006),
                ('Squirtle', 'Bubble', 'Aqua Tail', False, 3.120000000000001),
            ],
        ),
        (
            [
                ("Bulbasaur", "Vine Whip", "Power Whip"),
                ("Charmander", "Scratch", "Flamethrower"),
                ("Squirtle", "Bubble", "Aqua Tail"),
            ],
            [
                ('Bulbasaur', 'Vine Whip', 'Power Whip', True, 0.0),
                ('Charmander', 'Scratch', 'Flamethrower', True, 0.0),
                ('Squirtle', 'Bubble', 'Aqua Tail', True, 0.0)
            ],
        ),
    ]
)
def test_get_best_attacks(pokemons, expected_pokemon_eval):
    evals = main(pokemons)
    assert evals == expected_pokemon_eval
