import pytest

from midterm_A import kontrola


@pytest.mark.parametrize(
    ("souradnice", "validni"),
    [
        ([(0.2, 0.3, 0.2), (0, 1.0, 1), (-0.5, 1.112, 0.85)], True),
        ([(0.2, 0.3, True), (0, 1.0, 1), (-0.5, 1.112, 0.85)], False),
        ([(0.2, 0.3, 0.2), (0, 1.0, 1), (-0.5, "1.112", 0.85)], False),
        ([(0.2, False, 0.2), ("0", 1.0, 1), (-0.5, 1.112, "bubak")], False),
    ]
)

def test_assignment(souradnice, validni):
    assert kontrola(souradnice) == validni
