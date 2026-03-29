import pytest

from midterm_F import assign_size_category

POKEDEX = {
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
    }
}


@pytest.mark.parametrize(
    ("pokemon", "expected_measured_pokemon"),
    [
        (
            {"name": "Best buddy", "id": "7", "height": 0.2, "weight": 8.05, "IVs": (0, 11, 15)},
            {"name": "Best buddy", "id": "7", "height": 0.2, "weight": 8.05, "IVs": (0, 11, 15), "size": None},
        ),
        (
            {"name": "Best buddy", "id": "7", "height": 0.23, "weight": 8.55, "IVs": (2, 11, 15)},
            {"name": "Best buddy", "id": "7", "height": 0.23, "weight": 8.55, "IVs": (2, 11, 15), "size": "XXS"},
        ),
        (
            {"name": "Best buddy", "id": "7", "height": 0.30, "weight": 9.14, "IVs": (5, 11, 1)},
            {"name": "Best buddy", "id": "7", "height": 0.30, "weight": 9.14, "IVs": (5, 11, 1), "size": "XS"},
        ),
        (
            {"name": "Best buddy", "id": "7", "height": 0.54, "weight": 16.54, "IVs": (12, 14, 10)},
            {"name": "Best buddy", "id": "7", "height": 0.54, "weight": 16.54, "IVs": (12, 14, 10), "size": "M"},
        ),
        (
            {"name": "Best buddy", "id": "7", "height": 0.7, "weight": 18.87, "IVs": (13, 10, 9)},
            {"name": "Best buddy", "id": "7", "height": 0.7, "weight": 18.87, "IVs": (13, 10, 9), "size": "XL"},
        ),
        (
            {"name": "Best buddy", "id": "7", "height": 0.99, "weight": 20.15, "IVs": (15, 15, 15)},
            {"name": "Best buddy", "id": "7", "height": 0.99, "weight": 20.15, "IVs": (15, 15, 15), "size": "XXL"},
        ),
        (
            {"name": "Best buddy", "id": "7", "height": 1.2, "weight": 22.55, "IVs": (15, 15, 15)},
            {"name": "Best buddy", "id": "7", "height": 1.2, "weight": 22.55, "IVs": (15, 15, 15), "size": None},
        ),
    ],
)
def test_assign_size_category(pokemon, expected_measured_pokemon):
    measured_pokemon = assign_size_category(pokemon, POKEDEX)
    assert measured_pokemon == expected_measured_pokemon
