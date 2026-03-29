import pytest

from midterm_F import main


@pytest.mark.parametrize(
    ("pokemons", "pokedex_id", "size_category", "expected_sorted_competition", "expected_winner"),
    [
        (
            [
                {"name": "Virizion", "id": "640", "height": 4.2, "weight": 422.55, "IVs": (15, 15, 15)},
                {"name": "Best buddy", "id": "7", "height": 0.23, "weight": 8.55, "IVs": (0, 11, 15)},
                {"name": "BFF", "id": "7", "height": 0.23, "weight": 8.45, "IVs": (10, 11, 15)},
                {"name": "Bestie", "id": "7", "height": 0.3, "weight": 9.45, "IVs": (15, 11, 15)},
                {"name": "Whatever", "id": "7", "height": 0.30, "weight": 9.14, "IVs": (5, 11, 1)},
            ],
            "7",
            "XXS",
            [
                {"name": "Best buddy", "id": "7", "height": 0.23, "weight": 8.55, "IVs": (0, 11, 15), "size": "XXS",
                 "score": 270},
                {"name": "BFF", "id": "7", "height": 0.23, "weight": 8.45, "IVs": (10, 11, 15), "size": "XXS",
                 "score": 280},
            ],
            "BFF",
        ),
        (
            [
                {"name": "Virizion1", "id": "640", "height": 2.24, "weight": 216.54, "IVs": (12, 14, 10)},
                {"name": "Weepinbell", "id": "70", "height": 0.23, "weight": 8.55, "IVs": (0, 11, 15)},
                {"name": "Virizion2", "id": "640", "height": 2.44, "weight": 246.54, "IVs": (15, 15, 11)},
                {"name": "Virizion3", "id": "640", "height": 1.84, "weight": 196.54, "IVs": (10, 10, 10)},
                {"name": "Bulbasaur", "id": "1", "height": 0.30, "weight": 9.14, "IVs": (5, 11, 1)},
            ],
            "640",
            "M",
            [
                {"name": "Virizion1", "id": "640", "height": 2.24, "weight": 216.54, "IVs": (12, 14, 10), "size": "M",
                 "score": 553},
                {"name": "Virizion2", "id": "640", "height": 2.44, "weight": 246.54, "IVs": (15, 15, 11), "size": "M",
                 "score": 608},
                {"name": "Virizion3", "id": "640", "height": 1.84, "weight": 196.54, "IVs": (10, 10, 10), "size": "M",
                 "score": 460},
            ],
            "Virizion2"
        ),
    ],
)
def test_main(pokemons, pokedex_id, size_category, expected_sorted_competition, expected_winner):
    competition, winner = main(pokemons, pokedex_id, size_category)
    assert competition == expected_sorted_competition
    assert winner == expected_winner
