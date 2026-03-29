import pytest

from midterm_G import drinking


@pytest.mark.parametrize(
    ("karel_list", "pepa_list", "expected_karel_spending", "expected_pepa_spending"),
    [
        (["Plzen 12"], ["Plzen 12"], 50, 55.00000000000001),
        (
                ["Plzen 12", "Plzen 12", "Plzen 12"],
                ["Svijany 11", "Svijany 11", "Svijany 11"],
                163.74605000000003,
                113.47601265
        ),
        (["Starobrno 10", "Policka", "Branik"], ["Branik", "Policka", "Starobrno 10"], 80.05174679999999, 84.54784833),
        (
                ["Branik", "Gambrinus 10", "Dalesice", "Svijany 11", "Policka"],
                ["Dalesice", "Starobrno 10", "Svijany 11", "Policka", "Plzen 12"],
                152.00326226366218,
                185.06796734114766
        ),
        (["Branik"] * 10, ["Branik"] * 10, 327.2857113900346, 360.01428252903804),
    ]
)
def test_drinking(karel_list, pepa_list, expected_karel_spending, expected_pepa_spending):
    karel_spending, pepa_spending = drinking(karel_list, pepa_list)
    assert karel_spending == expected_karel_spending
    assert pepa_spending == expected_pepa_spending
