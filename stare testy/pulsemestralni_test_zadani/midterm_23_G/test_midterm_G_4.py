import pytest

from midterm_G import main


@pytest.mark.parametrize(
    ("karel", "pepa", "expected_message"),
    [
        (
            ['Starobrno 12', 'Svijany 11', 'Branik'],
            ['Plzen 12', 'Gambrinus 10', 'Dalesice'],
            "Bez penez do hospody nelez. Kamaradum chybi 4.678214215799983.\n",
        ),
        (
            ['Gambrinus 10', 'Starobrno 10', 'Dalesice'],
            ['Gambrinus 10', 'Svijany 11', 'Branik'],
            "Kazdy ma na svou utratu. Karlovi zbyde 0.25196757999999875, Pepovi zbyde 32.627654401200004.\n"
        ),
        (
            ['Gambrinus 10', 'Branik', 'Starobrno 10'],
            ['Starobrno 12', 'Svijany 11', 'Plzen 12'],
            "Spolecne maji na spolecnou utratu. Dohromady jim zbyde 8.31095220500002.\n"
        ),
    ]
)
def test_main(capsys, karel, pepa, expected_message):
    main(karel, pepa)
    captured = capsys.readouterr()
    assert captured.out == expected_message
