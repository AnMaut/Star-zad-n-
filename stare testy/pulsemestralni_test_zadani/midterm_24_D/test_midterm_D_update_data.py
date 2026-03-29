import pytest

from midterm_D import update_data


@pytest.mark.parametrize(
    ("new_patient_values", "patient_values_old", "weight_trend", "patient_values_new_sol", "weight_trend_sol"),
    [
        ({"weight": 77, "saturation": 99, "heart rate": 62}, [25, 50, 25], [71, 71, 71, 71, 71, 71, 71, 71],
         [77, 99, 62], [71, 71, 71, 71, 71, 71, 71, 71, 77]),
        ({"weight": 77, "saturation": 99, "heart rate": 62}, [25, 50, 25], [71, 71, 71, 71, 78, 72, 71, 71],
         [77, 99, 62], [71, 71, 71, 71, 78, 72, 71, 71, 77]),
        ({"weight": 87, "saturation": 95, "heart rate": 62}, [25, 50, 25], [71, 71, 71, 71, 71, 71, 71, 71],
         [87, 95, 62], [71, 71, 71, 71, 71, 71, 71, 71, 87]),
        ({"weight": 77, "saturation": 99, "heart rate": 52}, [25, 50, 25], [71, 71, 71, 71, 71, 71, 71, 71],
         [77, 99, 52], [71, 71, 71, 71, 71, 71, 71, 71, 77]),
        ({"weight": 77, "saturation": 99, "heart rate": 62}, [25, 50, 25], [71, 78], [77, 99, 62], [71, 78, 77]),
     ]
)
def test_update_data(new_patient_values, patient_values_old, weight_trend, patient_values_new_sol, weight_trend_sol):
    patient_values_new, weight_trend = update_data(new_patient_values, patient_values_old, weight_trend)
    assert patient_values_new == patient_values_new_sol
    assert weight_trend == weight_trend_sol
