POKEDEX = ["Bulbasaur", "Charmander", "Squirtle"]

FAST_ATTACK_NAMES = [
    ["Vine Whip", "Tackle"],
    ["Ember", "Scratch"],
    ["Tackle", "Bubble"],
]
FAST_ATTACK_STATS = [
    [(7, 6, 0.6), (5, 5, 0.5)],
    [(10, 10, 1), (6, 4, 0.5)],
    [(5, 5, 0.5), (12, 14, 1.2)],
]

CHARGED_ATTACK_NAMES = [
    ["Seed Bomb", "Sludge Bomb", "Power Whip"],
    ["Flamethrower", "Flame Charge", "Flame Burst"],
    ["Aqua Jet", "Aqua Tail", "Water Pulse"],
]
CHARGED_ATTACK_STATS = [
    [(55, 33, 2.1), (80, 50, 2.3), (90, 50, 2.6)],
    [(70, 50, 2.2), (70, 33, 3.8), (70, 50, 2.6)],
    [(45, 33, 2.6), (50, 33, 1.9), (70, 50, 3.2)],
]


...


if __name__ == "__main__":
    pokemons = [
        ("Bulbasaur", "Vine Whip", "Seed Bomb"),
        ("Charmander", "Ember", "Flame Charge"),
        ("Squirtle", "Tackle", "Aqua Jet")
    ]

    pokemon_eval = main(pokemons)
    print(pokemons)
    print(pokemon_eval)
