import pytest

from midterm_D import doctor_visit


@pytest.mark.parametrize(
    ("available_dates", "today", "message_sol"),
    [
        ({55, 58, 90}, 95, "Tento rok jiz neni volny termin, nebyl jste objednan."),
        ({55, 58, 90}, 1, "Byl jste objednan k prohlidce 55. den tohoto roku."),
        ({55, 58, 90}, 56, "Byl jste objednan k prohlidce 58. den tohoto roku."),
     ]
)
def test_doctor_visit(available_dates, today, message_sol):
    message = doctor_visit(available_dates, today)
    assert message == message_sol
