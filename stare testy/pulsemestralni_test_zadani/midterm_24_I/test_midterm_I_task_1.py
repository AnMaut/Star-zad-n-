import pytest

from midterm_I import read_data


@pytest.mark.parametrize(
    ("file_name", "expected_data"),
    [
        ("attendance.csv", [
            ["Name", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"],
            ["Student 1", "/", "/", "/", "/", "/", "/", "/", "/", "|", "/", "/", "/", "|"],
            ["Student 2", "/", "-", "-", "oml", "oml", "-", "oml", "-", "|", "oml", "-", "-", "|"]
        ]),
        ("points.csv", [
            ["Name", "HW01", "HW02", "HW03", "HW04", "HW05", "HW06", "HW07", "Midterm", "Midterm2", "HW08", "HW09",
             "HW10", "Final", "Final2"],
            ["Student 1", "2", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["Student 2", "2", "2", "2", "2", "2", "2", "2", "2", "23", "0", "0", "0", "30", ""]
        ]),
    ]
)
def test_read_data(file_name, expected_data):
    assert read_data(file_name)[:3] == expected_data
