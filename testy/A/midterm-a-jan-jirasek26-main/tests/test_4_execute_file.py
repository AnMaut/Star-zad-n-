import microscope_stage
from microscope_stage import execute_file


config = {'x': {'min': -5000, 'max': 5000}, 'y': {'min': -3000, 'max': 3000}, 'z': {'min': 0, 'max': 2000}}


def test_execute_file_within_range(tmp_path):
    file_path = tmp_path / "cmds.csv"
    file_path.write_text("x,y,z\n500,0,1000\n500,-200,1000\n500,-200,1100\n")

    result = execute_file(str(file_path), config)

    assert len(result) == 3
    assert result[0] == {'x': 500, 'y': 0, 'z': 1000}
    assert result[1] == {'x': 500, 'y': -200, 'z': 1000}
    assert result[2] == {'x': 500, 'y': -200, 'z': 1100}


def test_execute_file_calls_set_position(monkeypatch, tmp_path):
    calls = []

    def fake_set_position(x, y, z):
        calls.append((x, y, z))

    monkeypatch.setattr(microscope_stage, 'set_position', fake_set_position)

    file_path = tmp_path / "cmds.csv"
    file_path.write_text("x,y,z\n6000,4000,3000\n-6000,-4000,-100\n")

    result = execute_file(str(file_path), config)

    assert result[0] == {'x': 5000, 'y': 3000, 'z': 2000}
    assert result[1] == {'x': -5000, 'y': -3000, 'z': 0}
    assert calls == [(5000, 3000, 2000), (-5000, -3000, 0)]


def test_execute_file_with_clamp(tmp_path):
    file_path = tmp_path / "cmds.csv"
    file_path.write_text("x,y,z\n6000,4000,3000\n-6000,-4000,-100\n")

    result = execute_file(str(file_path), config)

    assert len(result) == 2
    assert result[0] == {'x': 5000, 'y': 3000, 'z': 2000}
    assert result[1] == {'x': -5000, 'y': -3000, 'z': 0}


def test_execute_file_0():
    result = execute_file('data/commands_0.csv', config)
    assert len(result) == 5
    assert result[-1] == {'x': 1500, 'y': 300, 'z': 1100}


def test_execute_file_1():
    result = execute_file('data/commands_1.csv', config)
    assert len(result) == 5
    assert result[-1] == {'x': -5000, 'y': -3000, 'z': 500}
