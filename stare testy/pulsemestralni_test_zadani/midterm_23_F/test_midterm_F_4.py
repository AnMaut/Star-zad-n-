import pytest
from midterm_F import get_alarm_decision

@pytest.mark.parametrize(
    ("is_error_list", "is_error_list_last", "is_above_threshold_list", "is_above_threshold_list_last", "freezers_names", "error_names", "high_temp_names"),
    [([False, False, False],
      [False, False, True],
      [False, False, True],
      [False, False, True],
      ['small1', 'small2', 'zmrzka'],
      [],
      ['zmrzka'],
      ),
     ([False, True, False],
      [False, True, True],
      [False, False, False],
      [False, False, True],
      ['small1', 'small2', 'zmrzka'],
      ['small2'],
      [],
      ),
     ([False, True, False, True, True],
      [False, True, True, False, True],
      [False, True, False, True, True],
      [False, True, True, True, True],
      ['lowtem', 'sample', 'zmrzka', 'cells1', 'small2'],
      ['sample', 'small2'],
      ['sample', 'cells1', 'small2'],
      ),


     ]
)
def test_midterm_f_4(is_error_list, is_error_list_last, is_above_threshold_list, is_above_threshold_list_last, freezers_names, error_names, high_temp_names):

    error_names_out, high_temp_names_out = get_alarm_decision(is_error_list, is_error_list_last, is_above_threshold_list, is_above_threshold_list_last, freezers_names)
    assert error_names_out == error_names
    assert high_temp_names_out == high_temp_names




