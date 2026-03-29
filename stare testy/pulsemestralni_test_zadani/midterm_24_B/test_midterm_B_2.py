import pytest

from midterm_B import nutrient_selection


@pytest.mark.parametrize(
    ("average_growth_rates", "selected_nutrients"),
    [
        ([5.0, 6.0, 8.0, 4.5, 3.0], ["Amino Acids", "Minerals", "Minerals", "Amino Acids", "Glucose"]),
        ([0.0, 3.0, 8.0, 4.5], ["Glucose", "Glucose", "Minerals", "Amino Acids"]),
        ([7.2, 12, 3, 1.5, 2], ["Minerals", "Minerals", "Glucose", "Glucose", "Glucose"]),
        ([2.2, 4.1, 3.5, 7, 12, 1.0, 5.0],
         ["Glucose", "Amino Acids", "Amino Acids", "Minerals", "Minerals", "Glucose", "Amino Acids"]),
        ([5.2, 6, 4, 8.2, 1], ["Minerals", "Minerals", "Amino Acids", "Minerals", "Glucose"]),
        ([3, 3.1, 2.99, 4.99, 5], ["Glucose", "Amino Acids", "Glucose", "Amino Acids", "Amino Acids"]),
        ([3, 3.1], ["Glucose", "Amino Acids"]),
    ]
)
def test_nutrient_selection(average_growth_rates, selected_nutrients):
    assert nutrient_selection(average_growth_rates) == selected_nutrients
