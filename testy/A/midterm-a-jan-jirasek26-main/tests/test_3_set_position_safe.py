import microscope_stage
from microscope_stage import set_position_safe


config = {'x': {'min': -5000, 'max': 5000}, 'y': {'min': -3000, 'max': 3000}, 'z': {'min': 0, 'max': 2000}}


def test_position_within_range():
    position = {'x': 100, 'y': 200, 'z': 500}
    result = set_position_safe(position, config)
    assert result == {'x': 100, 'y': 200, 'z': 500}


def test_set_position_safe_calls_set_position(monkeypatch):
    calls = []

    def fake_set_position(x, y, z):
        calls.append((x, y, z))

    monkeypatch.setattr(microscope_stage, 'set_position', fake_set_position)

    position = {'x': 6000, 'y': 4000, 'z': 3000}
    result = set_position_safe(position, config)

    assert result == {'x': 5000, 'y': 3000, 'z': 2000}
    assert calls == [(5000, 3000, 2000)]


def test_position_exceeds_max():
    position = {'x': 6000, 'y': 4000, 'z': 3000}
    result = set_position_safe(position, config)
    assert result == {'x': 5000, 'y': 3000, 'z': 2000}


def test_position_below_min():
    position = {'x': -6000, 'y': -4000, 'z': -100}
    result = set_position_safe(position, config)
    assert result == {'x': -5000, 'y': -3000, 'z': 0}


def test_position_at_boundary():
    position = {'x': -5000, 'y': 3000, 'z': 0}
    result = set_position_safe(position, config)
    assert result == {'x': -5000, 'y': 3000, 'z': 0}
