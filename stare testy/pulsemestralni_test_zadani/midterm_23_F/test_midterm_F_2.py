import pytest
from midterm_F import order

@pytest.mark.parametrize(
    ('measurement_timepoint_fix', 'freezers_names', 'measurement_timepoint_ordered'),
    [([('small1', -20.1), ('zmrzka', -16.2), ('large1', None), ('cells1', -62.2)],
      ['small1', 'small2', 'zmrzka', 'large1', 'cells1'],
      [('small1', -20.1), ('small2', None), ('zmrzka', -16.2), ('large1', None), ('cells1', -62.2)],
      ),
     ([('zmrzka', -11.3), ('cells1', -65.1), ('large1', None), ('small1', -17.2)],
      ['small1', 'small2', 'zmrzka', 'large1', 'cells1'],
      [('small1', -17.2), ('small2', None), ('zmrzka', -11.3), ('large1', None), ('cells1', -65.1)],
      ),
     ([('samples', None), ('lowtem', -33.3)],
      ['lowtem', 'sample', 'large1', 'cells1'],
      [('lowtem', -33.3), ('sample', None), ('large1', None), ('cells1', None)],
      ),
     ],
)
def test_midterm_f_2(measurement_timepoint_fix, freezers_names, measurement_timepoint_ordered):
    measurement_timepoint_ordered_out = order(measurement_timepoint_fix, freezers_names)
    assert measurement_timepoint_ordered_out == measurement_timepoint_ordered