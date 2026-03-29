import pytest
from midterm_C import main


@pytest.mark.parametrize(
    ("my_queue", "number_of_cluster_threads", "final_assignments", "rest_of_computer_resources"),
    [(
        [("xchmel10", 64, 32, 6), ("xnovak25", 12, 18, 2), ("xjakub77", 32, 64, 9), ("xharab22", 4, 12, 10),
         ("xkolar00", 1, 8, 10), ("xvitek07", 4, 40, 1), ("xsedla33", 1, 3, 5), ("xjanou03", 12, 32, 2),
         ("xchmel11", 14, 12, 7)],
        129,
        [('xharab22', 'C4'), ('xkolar00', 'C6'), ('xjakub77', 'C1'), ('xchmel11', 'C2'), ('xchmel10', 'C0'),
         ('xsedla33', 'C7'), ('xnovak25', None), ('xjanou03', None), ('xvitek07', None)],
        [['C2', 2, 52], ['C3', 8, 32], ['C5', 2, 8]]
      ),
     (
        [("xchmel10", 32, 12, 7), ("xnovak25", 22, 16, -1), ("xjakub77", 12, 12, 9), ("xharab22", 10, 64, 10),
         ("xkolar00", 1, 4, 10), ("xvitek07", 2, 40, 8), ("xsedla33", 3, 7, 6), ("xjanou03", 100, 100, 4),
         ("xchmel11", 32, 32, 9)],
        240,
        [('xharab22', 'C3'), ('xkolar00', 'C6'), ('xjakub77', 'C2'), ('xchmel11', 'C1'), ('xvitek07', 'C2'),
         ('xchmel10', 'C0'), ('xsedla33', 'C5'), ('xjanou03', None)],
        [['C0', 88, 468], ['C1', 28, 208], ['C2', 16, 68], ['C4', 8, 32], ['C5', 1, 9], ['C6', 1, 4]]
      )
     ]
)
def test_midterm_c_main(my_queue, number_of_cluster_threads, final_assignments, rest_of_computer_resources):

    final_assignments_out, rest_of_computer_resources_out = main(my_queue, number_of_cluster_threads)
    assert final_assignments_out == final_assignments
    assert rest_of_computer_resources_out == rest_of_computer_resources
