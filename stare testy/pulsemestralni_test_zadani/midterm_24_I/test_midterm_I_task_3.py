import pytest

from midterm_I import evaluate_points

HEADER = ["Name", "HW01", "HW02", "HW03", "HW04", "HW05", "HW06", "HW07", "Midterm", "Midterm2", "HW08", "HW09", "HW10",
          "Final", "Final2"]


@pytest.mark.parametrize(
    ("points", "expected_has_mins", "expected_points"),
    [
        (["Student 1", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], False, 0),
        (["Student 1", "2", "2", "2", "2", "2", "2", "2", "30", "", "2", "2", "2", "50", ""], True, 100),
        (["Student 1", "2", "2", "2", "2", "2", "2", "2", "10", "30", "2", "2", "2", "5", "50"], True, 100),
        (["Student 1", "", "", "", "", "", "", "", "10", "30", "", "", "", "5", "50"], True, 80),
        (["Student 1", "", "", "", "", "", "", "", "14", "15", "", "", "", "24", "25"], True, 40),
        (["Student 1", "", "", "", "", "", "", "", "14", "14", "", "", "", "24", "50"], False, 64),
        (["Student 1", "", "", "", "", "", "", "", "14", "20", "", "", "", "24", "24"], False, 44),
        (["Student 1", "0", "2", "2", "0", "0", "2", "2", "14", "25", "0", "2", "2", "24", "44"], True, 81),
    ]
)
def test_evaluate_points(points, expected_has_mins, expected_points):
    assert evaluate_points(HEADER, points) == (expected_has_mins, expected_points)
