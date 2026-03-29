import pytest

from midterm_B import genetic_modification_assessment


@pytest.mark.parametrize(
    ("selected_nutrients", "nutrient_modification_map", "genetic_modifications"),
    [
        (
            ["Glucose", "Amino Acids", "Glucose", "Amino Acids", "Amino Acids"],
            {"Amino Acids": "Gene Knockout", "Glucose": "Gene Overexpression", "Minerals": "Gene Editing"},
            ["Gene Overexpression", "Gene Knockout", "Gene Overexpression", "Gene Knockout", "Gene Knockout"]
        ),
        (
            ["Amino Acids", "Minerals", "Minerals", "Amino Acids", "Glucose"],
            {"Amino Acids": "Gene Knockout", "Glucose": "Gene Overexpression", "Minerals": "Gene Editing"},
            ["Gene Knockout", "Gene Editing", "Gene Editing", "Gene Knockout", "Gene Overexpression"]
        ),
        (
            ["Minerals", "Minerals", "Glucose", "Amino Acids", "Glucose", "Amino Acids"],
            {"Amino Acids": "Gene Knockout", "Glucose": "Gene Overexpression", "Minerals": "Gene Editing"},
            ["Gene Editing", "Gene Editing", "Gene Overexpression", "Gene Knockout", "Gene Overexpression",
             "Gene Knockout"]
        ),
        (
            ["Amino Acids", "Glucose", "Glucose"],
            {"Amino Acids": "Gene Knockout", "Glucose": "Gene Overexpression", "Minerals": "Gene Editing"},
            ["Gene Knockout", "Gene Overexpression", "Gene Overexpression"]
        ),
        (
            ["Amino Acids", "Glucose", "Glucose", "Minerals"],
            {"Amino Acids": "Gene Overexpression", "Glucose": "Gene Editing", "Minerals": "Gene Knockout"},
            ["Gene Overexpression", "Gene Editing", "Gene Editing", "Gene Knockout"]
        ),
    ]
)
def test_genetic_modification_assessment(selected_nutrients, nutrient_modification_map, genetic_modifications):
    assert genetic_modification_assessment(selected_nutrients, nutrient_modification_map) == genetic_modifications
