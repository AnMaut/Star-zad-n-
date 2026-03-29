import pytest

from midterm_B import main


@pytest.mark.parametrize(
    ("cell_sizes", "nutrient_modification_map", "cultures"),
    [
        (
            [[10, 15, 20, 25, 30], [12, 18, 24, 30, 36], [8, 14, 26, 32, 40], [11, 15.5, 20, 24.5, 29],
             [3, 6, 9.5, 12, 16], [1.5, 3.5, 5.5, 7.5, 9.5]],
            {"Amino Acids": "Gene Knockout", "Glucose": "Gene Overexpression", "Minerals": "Gene Editing"},
            [
                ("Culture 1", 5.0, "Amino Acids", "Gene Knockout"),
                ("Culture 2", 6.0, "Minerals", "Gene Editing"),
                ("Culture 3", 4.5, "Amino Acids", "Gene Knockout"),
                ("Culture 4", 2.0, "Glucose", "Gene Overexpression")
            ]
        ),
        (
            [[2, 4, 6, 8, 10], [24, 36, 48, 60, 72], [16, 32, 48, 64, 80], [22, 31, 40, 49, 58], [6, 12, 18, 24, 30]],
            {"Amino Acids": "Gene Knockout", "Glucose": "Gene Overexpression", "Minerals": "Gene Editing"},
            [
                ("Culture 1", 2.0, "Glucose", "Gene Overexpression"),
                ("Culture 2", 12.0, "Minerals", "Gene Editing"),
                ("Culture 3", 16.0, "Minerals", "Gene Editing"),
                ("Culture 4", 9.0, "Minerals", "Gene Editing"),
                ("Culture 5", 6.0, "Minerals", "Gene Editing")
            ]
        ),
        (
            [[2.5, 4.5, 6, 8.5, 10], [15, 30, 45, 60, 75], [1, 3, 4, 6, 20], [22, 31, 40, 49, 58]],
            {"Amino Acids": "Gene Knockout", "Glucose": "Gene Overexpression", "Minerals": "Gene Editing"},
            [
                ("Culture 1", 15.0, "Minerals", "Gene Editing"),
                ("Culture 2", 9.0, "Minerals", "Gene Editing")
            ]
        ),
        (
            [[6, 10, 14, 16.5, 20], [6, 8.5, 11, 13.5, 16], [1, 5, 9, 13, 17], [25, 30, 35, 40, 45],
             [0, 2, 4, 6, 8, 10]],
            {"Amino Acids": "Gene Knockout", "Glucose": "Gene Overexpression", "Minerals": "Gene Editing"},
            [
                ("Culture 1", 2.5, "Glucose", "Gene Overexpression"),
                ("Culture 2", 4.0, "Amino Acids", "Gene Knockout"),
                ("Culture 3", 5.0, "Amino Acids", "Gene Knockout"),
                ("Culture 4", 2.0, "Glucose", "Gene Overexpression")
            ]
        ),
    ]
)
def test_main(cell_sizes, nutrient_modification_map, cultures):
    assert main(cell_sizes, nutrient_modification_map) == cultures
