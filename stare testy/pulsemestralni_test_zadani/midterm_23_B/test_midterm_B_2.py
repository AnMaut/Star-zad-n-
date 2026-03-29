import pytest

from midterm_B import hebrejci


@pytest.mark.parametrize(
    ("message", "encoded_message"),
    [("Ahoj svete", "Zslq hevgv"),
     ("Nevim co dale otestovat", "Mvern xl wzov lgvhglezg"),
     ("Zslq hevgv", "Ahoj svete"),
     ("Mvern xl wzov lgvhglezg", "Nevim co dale otestovat"),
    ]
)
def test_hebrejci(message, encoded_message):
    assert hebrejci(message) == encoded_message
