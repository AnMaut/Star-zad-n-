import pytest

from midterm_B import uprava


@pytest.mark.parametrize(
    ("message", "expected_message"),
    [("Příliš žluťoučký kůň úpěl ďábelské ódy!", "Prilis zlutoucky kun upel dabelske ody"),
     ("Dnešek je tak krásný den, byla by škoda nejít ven.", "Dnesek je tak krasny den byla by skoda nejit ven"),
     ("Miluju programovat v Pythonu, Ty snad ne?", "Miluju programovat v Pythonu Ty snad ne"),
     ("Nechci vás vidět na opravném termínu!", "Nechci vas videt na opravnem terminu"),
     ("Python 4ever :-*", "Python ever "),
     ("20.3.@11:00", False),
    ]
)
def test_uprava(message, expected_message):
    assert uprava(message) == expected_message
