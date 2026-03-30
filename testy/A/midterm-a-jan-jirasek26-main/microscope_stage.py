from stage_simulator import set_position
import json
import csv

def read_stage_config(path):
    with open(path, "r") as file:
        config_dict = json.load(file)
    return config_dict

def get_home_position(configuration_dict):
    home_position = {}

    x_values = configuration_dict["x"]
    x_home = (x_values["min"] + x_values["max"]) / 2
    home_position["x"] = int(x_home)

    y_values = configuration_dict["y"]
    y_home = (y_values["min"] + y_values["max"]) / 2
    home_position["y"] = int(y_home)

    z_values = configuration_dict["z"]
    z_home = (z_values["min"] + z_values["max"]) / 2
    home_position["z"] = int(z_home)

    return home_position

def set_position_safe(position, configuration):
    updated_position = {}
    x_config = configuration["x"]
    y_config = configuration["y"]
    z_config = configuration["z"]

    if position["x"] < x_config["min"]:
        updated_position["x"] = x_config["min"]
    elif position["x"] > x_config["max"]:
        updated_position["x"] = x_config["max"]
    else:
        updated_position["x"] = position["x"]

    if position["y"] < y_config["min"]:
        updated_position["y"] = y_config["min"]
    elif position["y"] > y_config["max"]:
        updated_position["y"] = y_config["max"]
    else:
        updated_position["y"] = position["y"]

    if position["z"] < z_config["min"]:
        updated_position["z"] = z_config["min"]
    elif position["z"] > z_config["max"]:
        updated_position["z"] = z_config["max"]
    else:
        updated_position["z"] = position["z"]

    return updated_position

def execute_file(path, configuration):
    with open(path, "r") as file_csv:
        positions = []
        lines = file_csv.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split(","))

        i = 1
        while i < len(data):
            new_position = {}
            new_position["x"] = int(data[i][0])
            new_position["y"] = int(data[i][1])
            new_position["z"] = int(data[i][2])
            safe_pos = set_position_safe(new_position, configuration)
            positions.append(safe_pos)
            i += 1

    return positions

def plan_grid_scan(configuration, step_x, step_y, path):
    config_x = configuration["x"]
    x_min = config_x["min"]
    x_max = config_x["max"]
    config_y = configuration["y"]
    y_min = config_y["min"]
    y_max = config_y["max"]

    steps_x = []
    position_x = x_min
    while position_x <= x_max:
        steps_x.append(position_x)
        position_x = position_x + step_x

    steps_y = []
    position_y = y_min
    while position_y <= y_max:
        steps_y.append(position_y)
        position_y = position_y + step_y

    i = 0
    all_coordinates = []
    all_coordinates.append(["x", "y", "z"])
    while i < len(steps_x):
        coordinates = []
        coordinates.append(steps_x[i])
        j = 0
        while j < len(steps_y):
            coordinates.append(steps_y[j])
            j += 1

        coordinates.append(1000)
        all_coordinates.append(coordinates)

        i += 1

    with open(path, "w", newline="") as export_file:
        writer = csv.writer(export_file)
        writer.writerows(all_coordinates)

    steps_count = len(steps_x) * 3

    return steps_count

def main(configuration_path, grid_scan_path):
    configuration = read_stage_config(configuration_path)
    home_pos = get_home_position(configuration)
    safe_home_pos = set_position_safe(home_pos, configuration)
    steps_count = plan_grid_scan(configuration, 1000, 1000, grid_scan_path)
    positions = execute_file(grid_scan_path, configuration)

    print(f"Stage position set to: x={safe_home_pos['x']}, y={safe_home_pos['y']}, z={safe_home_pos['z']}")
    i = 0
    while i < len(positions):
        print(f"Stage position set to: x={positions[i]['x']}, y={positions[i]['y']}, z={positions[i]['z']}")
        i += 1

    print(f"Počet naplánovaných pozic pro grid scan: {steps_count}")

main("data/stage_config.json", "planned_grid_scan.csv")