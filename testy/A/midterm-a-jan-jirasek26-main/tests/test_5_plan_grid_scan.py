from microscope_stage import plan_grid_scan


config = {'x': {'min': -5000, 'max': 5000}, 'y': {'min': -3000, 'max': 3000}, 'z': {'min': 0, 'max': 2000}}


def test_plan_grid_scan_count(tmp_path):
    output_path = tmp_path / "grid_scan.csv"

    result = plan_grid_scan(config, 5000, 3000, str(output_path))

    # x: -5000, 0, 5000 (3 values)
    # y: -3000, 0, 3000 (3 values)
    assert result == 9


def test_plan_grid_scan_positions(tmp_path):
    output_path = tmp_path / "grid_scan.csv"

    plan_grid_scan(config, 5000, 3000, str(output_path))

    with open(output_path, "r", encoding="utf-8") as file_handle:
        rows = [line.strip().split(",") for line in file_handle if line.strip()][1:]

    assert rows[0] == ['-5000', '-3000', '1000']
    assert rows[1] == ['0', '-3000', '1000']
    assert rows[2] == ['5000', '-3000', '1000']
    assert rows[3] == ['-5000', '0', '1000']
    assert rows[-1] == ['5000', '3000', '1000']


def test_plan_grid_scan_small(tmp_path):
    small_config = {'x': {'min': 0, 'max': 10}, 'y': {'min': 0, 'max': 10}, 'z': {'min': 0, 'max': 100}}
    output_path = tmp_path / "grid_scan.csv"

    result = plan_grid_scan(small_config, 5, 5, str(output_path))

    with open(output_path, "r", encoding="utf-8") as file_handle:
        rows = [line.strip().split(",") for line in file_handle if line.strip()][1:]

    # x: 0, 5, 10 (3 values)
    # y: 0, 5, 10 (3 values)
    assert result == 9
    assert rows[0] == ['0', '0', '50']
    assert rows[-1] == ['10', '10', '50']
