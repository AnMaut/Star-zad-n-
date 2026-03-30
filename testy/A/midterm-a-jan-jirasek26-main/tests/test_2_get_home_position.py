from microscope_stage import get_home_position


config_1 = {'x': {'min': -5000, 'max': 5000}, 'y': {'min': -3000, 'max': 3000}, 'z': {'min': 0, 'max': 2000}}
home_1 = {'x': 0, 'y': 0, 'z': 1000}

config_2 = {'x': {'min': 0, 'max': 100}, 'y': {'min': 0, 'max': 200}, 'z': {'min': 100, 'max': 300}}
home_2 = {'x': 50, 'y': 100, 'z': 200}

config_3 = {'x': {'min': -10, 'max': 10}, 'y': {'min': -10, 'max': 10}, 'z': {'min': -10, 'max': 10}}
home_3 = {'x': 0, 'y': 0, 'z': 0}


def test_get_home_position():
    assert get_home_position(config_1) == home_1
    assert get_home_position(config_2) == home_2
    assert get_home_position(config_3) == home_3
