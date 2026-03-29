import pytest
from midterm_C import assign_request


@pytest.mark.parametrize(
    ("available_computers", "queue", "remaining_computers", "assignment", "queue_new"),
    [(
        [['C0', 28, 112], ['C1', 14, 56], ['C2', 8, 32], ['C3', 4, 16], ['C4', 2, 8]],
        [('xchmel10', 64, 32, 6), ('xnovak25', 12, 18, 2), ('xjakub77', 32, 64, 9), ('xvitek07', 4, 40, 1),
         ('xsedla33', 1, 3, 5), ('xjanou03', 12, 32, 2), ('xchmel11', 14, 12, 7)],
        [['C0', 28, 112], ['C1', 14, 56], ['C2', 8, 32], ['C3', 4, 16], ['C4', 2, 8]],
        ('xjakub77', None),
        [('xchmel10', 64, 32, 6), ('xnovak25', 12, 18, 2), ('xvitek07', 4, 40, 1), ('xsedla33', 1, 3, 5),
         ('xjanou03', 12, 32, 2), ('xchmel11', 14, 12, 7)]
      ),
     (
        [['C0', 20, 80], ['C1', 10, 40], ['C2', 6, 24], ['C3', 4, 16], ['C4', 1, 4]],
        [('xnovak25', 12, 18, 2), ('xvitek07', 4, 40, 1), ('xsedla33', 1, 3, 5), ('xjanou03', 12, 32, 2)],
        [['C0', 20, 80], ['C1', 10, 40], ['C2', 6, 24], ['C3', 4, 16]],
        ('xsedla33', 'C4'),
        [('xnovak25', 12, 18, 2), ('xvitek07', 4, 40, 1), ('xjanou03', 12, 32, 2)]
      ),
     (
        [['C0', 50, 200], ['C1', 26, 104], ['C2', 14, 56], ['C3', 8, 32], ['C4', 1, 4]],
        [('xvitek07', 4, 40, 1), ('xjanou03', 12, 32, 2)],
        [['C0', 50, 200], ['C1', 26, 104], ['C2', 2, 24], ['C3', 8, 32], ['C4', 1, 4]],
        ('xjanou03', 'C2'),
        [('xvitek07', 4, 40, 1)]
      ),
     (
        [['C0', 66, 264], ['C1', 34, 136], ['C2', 18, 72], ['C3', 10, 40], ['C4', 6, 24]],
        [('xchmel10', 32, 12, 5), ('xnovak25', 22, 16, 1), ('xjakub77', 12, 12, 11), ('xvitek07', 2, 40, 8),
         ('xsedla33', 3, 7, 6), ('xjanou03', 100, 100, 4), ('xchmel11', 32, 32, -1)],
        [['C0', 66, 264], ['C1', 34, 136], ['C2', 18, 72], ['C4', 6, 24]],
        ('xvitek07', 'C3'),
        [('xchmel10', 32, 12, 5), ('xnovak25', 22, 16, 1), ('xsedla33', 3, 7, 6), ('xjanou03', 100, 100, 4)]
      ),
     (
        [['C0', 6, 24], ['C1', 4, 16], ['C2', 2, 8]],
        [('xjakub77', 12, 12, 9), ('xharab22', 10, 64, 10), ('xkolar00', 1, 4, 10)],
        [['C0', 6, 24], ['C1', 4, 16], ['C2', 2, 8]],
        ('xharab22', None),
        [('xjakub77', 12, 12, 9), ('xkolar00', 1, 4, 10)]
      )
     ]
)
def test_midterm_c_main(available_computers, queue, remaining_computers, assignment, queue_new):

    assignment_out, remaining_computers_out, queue_new_out = assign_request(available_computers, queue)
    assert assignment_out == assignment
    assert remaining_computers_out == remaining_computers
    assert queue_new_out == queue_new
