import pytest

from midterm_F import get_score


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
    ("pokemon", "expected_scored_pokemon"),
    [
        (
            {"name": "Best buddy", "id": "7", "height": 0.2, "weight": 8.05, "IVs": (0, 11, 15)},
            {"name": "Best buddy", "id": "7", "height": 0.2, "weight": 8.05, "IVs": (0, 11, 15), "score": 243},
        ),
        (
            {"name": "Best buddy", "id": "7", "height": 0.23, "weight": 8.55, "IVs": (2, 11, 15)},
            {"name": "Best buddy", "id": "7", "height": 0.23, "weight": 8.55, "IVs": (2, 11, 15), "score": 272},
        ),
        (
            {"name": "Best buddy", "id": "7", "height": 0.30, "weight": 9.14, "IVs": (5, 11, 1)},
            {"name": "Best buddy", "id": "7", "height": 0.30, "weight": 9.14, "IVs": (5, 11, 1), "score": 320},
        ),
        (
            {"name": "Best buddy", "id": "640", "height": 2.24, "weight": 216.54, "IVs": (12, 14, 10)},
            {"name": "Best buddy", "id": "640", "height": 2.24, "weight": 216.54, "IVs": (12, 14, 10), "score": 553},
        ),
        (
            {"name": "Best buddy", "id": "640", "height": 2.57, "weight": 268.87, "IVs": (13, 10, 9)},
            {"name": "Best buddy", "id": "640", "height": 2.57, "weight": 268.87, "IVs": (13, 10, 9), "score": 630},
        ),
        (
            {"name": "Best buddy", "id": "640", "height": 3.99, "weight": 380.15, "IVs": (15, 14, 15), "size": "XXL"},
            {"name": "Best buddy", "id": "640", "height": 3.99, "weight": 380.15, "IVs": (15, 14, 15), "size": "XXL",
             "score": 961},
        ),
        (
            {"name": "Best buddy", "id": "640", "height": 4.2, "weight": 422.55, "IVs": (15, 15, 15)},
            {"name": "Best buddy", "id": "640", "height": 4.2, "weight": 422.55, "IVs": (15, 15, 15), "score": 1017},
        ),
    ],
)
def test_get_score(pokemon, expected_scored_pokemon):
    scored_pokemon = get_score(pokemon, POKEDEX)
    assert scored_pokemon == expected_scored_pokemon
