import pytest
from midterm_F import check_if_above_threshold

@pytest.mark.parametrize(
    ("measurement_timepoint_ordered", "is_error_list", "is_above_threshold_list"),
    [([('small1', -20.1), ('zmrzka', -9.2), ('large1', None), ('cells1', -62.2)],
      [False, False, True, False],
      [False, True, False, False],
      ),
     ([('zmrzka', -11.3), ('cells1', -65.1), ('large1', None), ('small1', -17.2)],
      [False, False, True, False],
      [True, False, False, False],
      ),
     ([('lowtem', -33.3), ('sample', None), ('large1', None)],
      [False, True, True],
      [True, False, False],
      ),
     ],
)
def test_assignment_f_3(measurement_timepoint_ordered,  is_error_list, is_above_threshold_list):

    is_error_list_out, is_above_threshold_list_out = check_if_above_threshold(measurement_timepoint_ordered)
    assert is_error_list_out == is_error_list
    assert is_above_threshold_list_out == is_above_threshold_list

