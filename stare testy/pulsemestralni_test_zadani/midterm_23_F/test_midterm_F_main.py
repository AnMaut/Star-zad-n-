import pytest
from midterm_F import main

@pytest.mark.parametrize(
    ("sensors_stream", "freezers_names", "error_names_all", "high_temp_names_all"),
    [([
        [('small1', -20.1), ('zmrwka', -16.2), ('large1', None), ('cells1', -62.2), ],
        [('lawge1', -21.8), ('small1', -19.7), ('zmrzka', -12.6), ('small2', -22.7), ('cells1', -63.5), ],
        [('zmrzka', -11.3), ('celws1', -65.1), ('large1', None), ('smggl1', -17.2), ],
        [('laree1', None), ('small1', -22.8), ('zmrjka', -10.3), ('cllls1', -66.3), ],
        ],
      ['small1', 'small2', 'zmrzka', 'large1', 'cells1'],
      [[], [], [],  ['small2', 'large1']],
      [[], [], ['zmrzka'], ['zmrzka']],
      ),
     ]
)
def test_midterm_f_main(sensors_stream, freezers_names, error_names_all, high_temp_names_all):

    error_names_all_out, high_temp_names_all_out = main(sensors_stream, freezers_names)
    assert error_names_all_out == error_names_all
    assert high_temp_names_all_out == high_temp_names_all




