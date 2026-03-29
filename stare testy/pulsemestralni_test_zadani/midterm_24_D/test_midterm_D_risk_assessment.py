import pytest

from midterm_D import risk_assessment


@pytest.mark.parametrize(
    ("patient_values_new", "weight_trend", "risk_sol"),
    [
        ([71, 100, 60], [71, 71, 71, 71, 71, 71, 71, 71], 0),
        ([71, 100, 60], [75, 71, 71, 71, 71, 71, 71, 71], 0),
        ([75, 100, 60], [71, 71, 71, 71, 71, 71, 71, 75], 4),
        ([71, 80, 60], [71, 71, 71, 71, 71, 71, 71, 71], 10),
        ([121, 99, 125], [121, 71, 71, 71, 71, 110, 130, 121], 10),
        ([121, 99, 125], [71, 71, 71, 71, 71, 110, 130, 121], 60),
        ([121, 89, 125], [71, 71, 71, 71, 71, 110, 130, 121], 70),
     ]
)
def test_risk_assessment(patient_values_new, weight_trend, risk_sol):
    risk = risk_assessment(patient_values_new, weight_trend)
    assert risk == risk_sol
