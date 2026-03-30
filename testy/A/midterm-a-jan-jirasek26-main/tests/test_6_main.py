from microscope_stage import main


def test_main_output_for_file_0(capsys, tmp_path):
    output_path = tmp_path / 'planned_grid_scan.csv'

    main('data/stage_config.json', str(output_path))

    captured = capsys.readouterr().out
    expected_lines = [
        'Stage position set to: x=0, y=0, z=1000',
    ]

    for y in range(-3000, 3001, 1000):
        for x in range(-5000, 5001, 1000):
            expected_lines.append(f'Stage position set to: x={x}, y={y}, z=1000')

    expected_lines.append('Počet naplánovaných pozic pro grid scan: 77')

    assert captured == '\n'.join(expected_lines) + '\n'