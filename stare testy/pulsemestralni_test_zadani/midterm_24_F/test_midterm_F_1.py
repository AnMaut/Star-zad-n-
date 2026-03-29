from midterm_F import load_pokedex


def test_load_pokedex():
    pokedex = load_pokedex("pokedex.json")
    assert isinstance(pokedex, dict)
    assert len(pokedex) == 649
    assert isinstance(pokedex["10"], dict)
    assert len(pokedex["111"]) == 14
    