import pytest

from midterm_F import get_competitors


POKEDEX = {
    "7": {
        "Name": "Squirtle",
        "Stamina": 127,
        "Attack": 94,
        "Defense": 121,
        "Primary": "Water",
        "Secondary": None,
        "MaxHP": 112,
        "Capture_rate": 0.2,
        "Escape_rate": 0.1,
        "Weight": 9.0,
        "Height": 0.5,
        "Legendary": "No",
        "MaxCP": 946,
        "Generation": 1
    },
    "640": {
        "Name": "Virizion",
        "Stamina": 209,
        "Attack": 192,
        "Defense": 229,
        "Primary": "Grass",
        "Secondary": "Fighting",
        "MaxHP": 177,
        "Capture_rate": 0.02,
        "Escape_rate": 0.01,
        "Weight": 200.0,
        "Height": 2.0,
        "Legendary": "Yes",
        "MaxCP": 3022,
        "Generation": 5
    },
}


@pytest.mark.parametrize(
    ("pokemons", "pokedex_id", "size_category", "expected_competitors"),
    [
        (
            [
                {"name": "Best buddy", "id": "640", "height": 4.2, "weight": 422.55, "IVs": (15, 15, 15)},
                {"name": "Best buddy", "id": "7", "height": 0.23, "weight": 8.55, "IVs": (0, 11, 15)},
                {"name": "Best buddy", "id": "7", "height": 0.23, "weight": 8.45, "IVs": (10, 11, 15)},
                {"name": "Best buddy", "id": "7", "height": 0.3, "weight": 9.45, "IVs": (15, 11, 15)},
                {"name": "Best buddy", "id": "7", "height": 0.30, "weight": 9.14, "IVs": (5, 11, 1)},
            ],
            "7",
            "XXS",
            [
                {"name": "Best buddy", "id": "7", "height": 0.23, "weight": 8.55, "IVs": (0, 11, 15), "size": "XXS",
                 "score": 270},
                {"name": "Best buddy", "id": "7", "height": 0.23, "weight": 8.45, "IVs": (10, 11, 15), "size": "XXS",
                 "score": 280},
            ]
        ),
        (
            [
                {"name": "Best buddy", "id": "640", "height": 2.24, "weight": 216.54, "IVs": (12, 14, 10)},
                {"name": "Best buddy", "id": "70", "height": 0.23, "weight": 8.55, "IVs": (0, 11, 15)},
                {"name": "Best buddy", "id": "640", "height": 2.44, "weight": 246.54, "IVs": (15, 15, 11)},
                {"name": "Best buddy", "id": "640", "height": 1.84, "weight": 196.54, "IVs": (10, 10, 10)},
                {"name": "Best buddy", "id": "1", "height": 0.30, "weight": 9.14, "IVs": (5, 11, 1)},
            ],
            "640",
            "M",
            [
                {"name": "Best buddy", "id": "640", "height": 2.24, "weight": 216.54, "IVs": (12, 14, 10), "size": "M",
                 "score": 553},
                {"name": "Best buddy", "id": "640", "height": 2.44, "weight": 246.54, "IVs": (15, 15, 11), "size": "M",
                 "score": 608},
                {"name": "Best buddy", "id": "640", "height": 1.84, "weight": 196.54, "IVs": (10, 10, 10), "size": "M",
                 "score": 460},
            ]
        ),
    ],
)
def test_get_score(pokemons, pokedex_id, size_category, expected_competitors):
    competitors = get_competitors(pokemons, POKEDEX, pokedex_id, size_category)
    assert competitors == expected_competitors
