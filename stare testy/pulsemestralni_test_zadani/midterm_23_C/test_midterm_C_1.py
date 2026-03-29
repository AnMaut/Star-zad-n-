import pytest
from midterm_C import create_cluster


@pytest.mark.parametrize(
    ("number_of_threads", "computer_list", "number_of_computers"),
    [(
        28,
        [['C0', 14, 56], ['C1', 8, 32], ['C2', 4, 16], ['C3', 2, 8]],
        4,
      ),
     (
        73,
        [['C0', 36, 144], ['C1', 18, 72], ['C2', 10, 40], ['C3', 4, 16], ['C4', 2, 8], ['C5', 2, 8], ['C6', 1, 4]],
        7,
      ),
     (
        96,
        [['C0', 48, 192], ['C1', 24, 96], ['C2', 12, 48], ['C3', 6, 24], ['C4', 4, 16], ['C5', 2, 8]],
        6,
      ),
     (
        129,
        [['C0', 64, 256], ['C1', 32, 128], ['C2', 16, 64], ['C3', 8, 32], ['C4', 4, 16], ['C5', 2, 8], ['C6', 2, 8],
         ['C7', 1, 4]],
        8,
      ),
     (
        1,
        [['C0', 1, 4]],
        1,
      )
     ]
)
def test_midterm_c_main(number_of_threads, computer_list, number_of_computers):

    computer_list_out, number_of_computers_out = create_cluster(number_of_threads)
    assert computer_list_out == computer_list
    assert number_of_computers_out == number_of_computers
