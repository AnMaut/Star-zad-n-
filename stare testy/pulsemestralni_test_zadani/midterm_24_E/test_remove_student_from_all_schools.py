import pytest
from assignment import remove_student_from_all_schools


LOADED_DATA_1 = {
    "Křenka": [["Barbora", 1], ["Adam", 2], ["Dana", 2], ["Gabriela", 1], ["Eva", 2]], 
    "Purkyňka": [["Barbora", 2], ["Ctirad", 1], ["Adam", 1], ["Helena", 1], ["Filip", 1], ["Ivan", 2]],
    "Jaroška": [["Ctirad", 2], ["Helena", 2], ["Dana", 1], ["Filip", 2], ["Gabriela", 2], ["Ivan", 1], ["Eva", 1]],
}

# Barbora removed
LOADED_DATA_STUDENT_REMOVED_1 = {
    "Křenka": [["Adam", 2], ["Dana", 2], ["Gabriela", 1], ["Eva", 2]], 
    "Purkyňka": [["Ctirad", 1], ["Adam", 1], ["Helena", 1], ["Filip", 1], ["Ivan", 2]],
    "Jaroška": [["Ctirad", 2], ["Helena", 2], ["Dana", 1], ["Filip", 2], ["Gabriela", 2], ["Ivan", 1], ["Eva", 1]],
}


LOADED_DATA_2 = {
    "Křenka": [["Barbora", 1], ["Adam", 2], ["Gabriela", 1], ["Eva", 2]], 
    "Purkyňka": [["Barbora", 2], ["Ctirad", 1], ["Adam", 1], ["Helena", 1], ["Filip", 1]],
    "Jaroška": [["Ctirad", 2], ["Helena", 2], ["Filip", 2], ["Gabriela", 2], ["Eva", 1]],
}

# Adam removed
LOADED_DATA_STUDENT_REMOVED_2 = {
    "Křenka": [["Barbora", 1], ["Gabriela", 1], ["Eva", 2]], 
    "Purkyňka": [["Barbora", 2], ["Ctirad", 1], ["Helena", 1], ["Filip", 1]],
    "Jaroška": [["Ctirad", 2], ["Helena", 2], ["Filip", 2], ["Gabriela", 2], ["Eva", 1]],
}


@pytest.mark.parametrize(
    ("loaded_data", "student_name", "loaded_data_student_removed_correct"),
    [
        (LOADED_DATA_1, "Barbora", LOADED_DATA_STUDENT_REMOVED_1),
        (LOADED_DATA_2, "Adam", LOADED_DATA_STUDENT_REMOVED_2),
    ]
)
def test_remove_student_from_all_schools(loaded_data, student_name, loaded_data_student_removed_correct):
    loaded_data_student_removed = remove_student_from_all_schools(loaded_data, student_name)
    assert loaded_data_student_removed == loaded_data_student_removed_correct
