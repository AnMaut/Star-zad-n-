import os


def set_position(x, y, z):
    print(f"Stage position set to: x={x}, y={y}, z={z}")

    log_path = os.getenv("STAGE_POSITION_LOG_PATH")
    if log_path:
        with open(log_path, "a", encoding="utf-8") as file_handle:
            file_handle.write(f"{x},{y},{z}\n")