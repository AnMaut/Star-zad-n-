import pytest

from midterm_I import evaluate_attendance


@pytest.mark.parametrize(
    ("attendance", "expected_was_present", "expected_perc"),
    [
        (["Student 1", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"], False, 0.00),
        (["Student 2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"], True, 100.00),
        (["Student 1", "/", "/", "/", "/", "/", "/", "|", "/", "/", "/", "/", "/", "|"], False, 0.00),
        (["Student 2", "/", "-", "-", "oml", "oml", "-", "oml", "-", "|", "oml", "-", "-", "|"], True, 90.91),
        (["Student 2", "-", "-", "-", "-", "-", "-", "-", "-", "|", "-", "-", "/", "|"], True, 90.91),
        (["Student 25", "-", "/", "-", "-", "-", "oml", "oml", "-", "-", "-", "-", "/", "-"], False, 84.62),
    ]
)
def test_evaluate_attendance(attendance, expected_was_present, expected_perc):
    was_present, perc = evaluate_attendance(attendance)
    assert was_present == expected_was_present
    assert round(perc, 2) == expected_perc


@pytest.mark.parametrize(
    ("attendance", "threshold", "expected_was_present", "expected_perc"),
    [
        (["Student 2", "/", "-", "-", "oml", "oml", "-", "oml", "-", "|", "oml", "-", "-", "|"], 95, False, 90.91),
        (["Student 2", "-", "-", "-", "oml", "-", "-", "-", "-", "|", "-", "/", "/", "|"], 80, True, 81.82),
        (["Student 25", "-", "/", "-", "-", "-", "/", "/", "-", "/", "-", "-", "/", "-"], 60, True, 61.54),
    ]
)
def test_evaluate_attendance2(attendance, threshold, expected_was_present, expected_perc):
    was_present, perc = evaluate_attendance(attendance, threshold)
    assert was_present == expected_was_present
    assert round(perc, 2) == expected_perc
