import pytest
from midterm_F import fix_names


@pytest.mark.parametrize(
    ('measurement_timepoint', 'freezers_names', 'measurement_timepoint_fix'),
    [([('smael1', -20.1), ('zmrwka', -16.2), ('large1', None), ('cells1', -62.2)],
      ['small1', 'small2', 'zmrzka', 'large1', 'cells1'],
      [('small1', -20.1), ('zmrzka', -16.2), ('large1', None), ('cells1', -62.2)],
      ),
     ([('zmrzka', -11.3), ('celws1', -65.1), ('large1', None), ('smggl1', -17.2)],
       ['small1', 'small2', 'zmrzka', 'large1', 'cells1'],
       [('zmrzka', -11.3), ('cells1', -65.1), ('large1', None), ('small1', -17.2)],
       ),
     ([('sample', None), ('lowttt', -33.3)],
       ['sample', 'lowtem'],
       [('sample', None), ('lowtem', -33.3)],
       ),
     ],

)
def test_midterm_f_1(measurement_timepoint, freezers_names, measurement_timepoint_fix):
    measurement_timepoint_fix_out = fix_names(measurement_timepoint, freezers_names)

    assert measurement_timepoint_fix_out == measurement_timepoint_fix
