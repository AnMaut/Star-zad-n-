import pytest

from midterm_G import payment


@pytest.mark.parametrize(
    ("karel_spending", "pepa_spending", "karel_money", "pepa_money", "expected_message"),
    [
        (50, 56, 50, 56, "Kazdy ma na svou utratu. Karlovi zbyde 0, Pepovi zbyde 0."),
        (50, 50, 100, 156, "Kazdy ma na svou utratu. Karlovi zbyde 50, Pepovi zbyde 106."),
        (50.28, 80.89, 150, 90, "Kazdy ma na svou utratu. Karlovi zbyde 99.72, Pepovi zbyde 9.11."),
        (50, 80, 120, 10, "Spolecne maji na spolecnou utratu. Dohromady jim zbyde 0."),
        (50, 80, 0, 200, "Spolecne maji na spolecnou utratu. Dohromady jim zbyde 70."),
        (10, 800, 1000, 0, "Spolecne maji na spolecnou utratu. Dohromady jim zbyde 190."),
        (50, 80, 0, 0, "Bez penez do hospody nelez. Kamaradum chybi 130."),
        (50, 80, 129, 0, "Bez penez do hospody nelez. Kamaradum chybi 1."),
        (50, 80, 0, 129, "Bez penez do hospody nelez. Kamaradum chybi 1."),
        (50, 80, 58, 16, "Bez penez do hospody nelez. Kamaradum chybi 56."),
    ]
)
def test_payment(karel_spending, pepa_spending, karel_money, pepa_money, expected_message):
    assert payment(karel_spending, pepa_spending, karel_money, pepa_money) == expected_message
