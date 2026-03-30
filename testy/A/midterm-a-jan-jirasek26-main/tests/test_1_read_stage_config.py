from microscope_stage import read_stage_config


def test_read_stage_config(tmp_path):
    config_path = tmp_path / "test_config.json"
    config_path.write_text('{"x": {"min": -100, "max": 100}, "y": {"min": -50, "max": 50}, "z": {"min": 0, "max": 200}}')

    result = read_stage_config(str(config_path))

    assert result == {'x': {'min': -100, 'max': 100}, 'y': {'min': -50, 'max': 50}, 'z': {'min': 0, 'max': 200}}


def test_read_stage_config_file():
    result = read_stage_config('data/stage_config.json')

    assert result['x']['min'] == -5000
    assert result['x']['max'] == 5000
    assert result['y']['min'] == -3000
    assert result['y']['max'] == 3000
    assert result['z']['min'] == 0
    assert result['z']['max'] == 2000
