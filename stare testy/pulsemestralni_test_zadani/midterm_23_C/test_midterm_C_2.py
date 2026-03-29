import pytest
from midterm_C import assign_computer


@pytest.mark.parametrize(
    ("available_computers", "user_request", "remaining_computers", "assignment"),
    [(
        [['C0', 36, 144], ['C1', 18, 72], ['C2', 10, 40], ['C3', 6, 24], ['C4', 4, 16]],
        ('xharab22', 10, 64, 10),
        [['C0', 36, 144], ['C1', 8, 8], ['C2', 10, 40], ['C3', 6, 24], ['C4', 4, 16]],
        ('xharab22', 'C1')
      ),
     (
        [['C0', 64, 256], ['C1', 32, 128], ['C2', 16, 64], ['C3', 8, 32], ['C4', 4, 16], ['C5', 2, 8], ['C6', 2, 8],
         ['C7', 1, 4]],
        ('xchmel11', 32, 32, 9),
        [['C0', 64, 256], ['C2', 16, 64], ['C3', 8, 32], ['C4', 4, 16], ['C5', 2, 8], ['C6', 2, 8],
         ['C7', 1, 4]],
        ('xchmel11', 'C1')
      ),
     (
        [['C0', 4, 16], ['C1', 2, 8], ['C2', 1, 4]],
        ('xchmel10', 32, 12, 7),
        [['C0', 4, 16], ['C1', 2, 8], ['C2', 1, 4]],
        ('xchmel10', None)
      ),
     (
        [['C0', 12, 48], ['C1', 6, 24], ['C2', 4, 16], ['C3', 1, 4]],
        ('xvitek07', 2, 40, 8),
        [['C0', 10, 8], ['C1', 6, 24], ['C2', 4, 16], ['C3', 1, 4]],
        ('xvitek07', 'C0')
      ),
     (
        [['C0', 2, 8]],
        ('xnovak25', 2, 8, 1),
        [],
        ('xnovak25', 'C0')
      )
     ]
)
def test_midterm_c_main(available_computers, user_request, remaining_computers, assignment):

    remaining_computers_out, assignment_out = assign_computer(available_computers, user_request)
    assert remaining_computers_out == remaining_computers
    assert assignment_out == assignment
