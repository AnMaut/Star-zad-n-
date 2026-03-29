import pytest

from midterm_G import order_beer


@pytest.mark.parametrize(
    ("beer_name", "beer_prices", "beer_names", "expected_beer_prices", "expected_beer_price"),
    [
        ("Plzen 12", [50], ["Plzen 12"], [55.00000000000001], 50),
        ("Plzen", [35, 15, 30], ["Plzen", "Gambrinus", "Svijany"], [38.5, 14.85, 29.7], 35),
        (
                "Svijany",
                [41.5, 20.8, 16.11, 46],
                ["Bernard", "Staropramen", "Branik", "Svijany"],
                [41.085, 20.592, 15.9489, 50.6],
                46
        ),
        (
                "Starobrno 10",
                [50, 20, 35, 12, 30, 40, 38, 42],
                ["Plzen 12", "Gambrinus", "Svijany", "Branik", "Starobrno 10", "Starobrno 12", "Policka", "Dalesice"],
                [49.5, 19.8, 34.65, 11.879999999999999, 33.0, 39.6, 37.62, 41.58],
                30
        ),
    ]
)
def test_order_beer(beer_name, beer_prices, beer_names, expected_beer_prices, expected_beer_price):
    new_beer_prices, one_beer_price = order_beer(beer_name, beer_prices, beer_names)
    assert new_beer_prices == expected_beer_prices
    assert one_beer_price == expected_beer_price
