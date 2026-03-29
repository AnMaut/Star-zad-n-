import pytest
from assignment import get_students_results_dict


SCHOOLS = ["Křenka", "Purkyňka", "Jaroška"]
SCHOOL_MAX_STUDENTS = [3, 2, 2]
NEZARAZEN = "nezařazen"


LOADED_DATA_1 = {
    "Křenka": [["Barbora", 1], ["Adam", 2], ["Dana", 2], ["Gabriela", 1], ["Eva", 2]], 
    "Purkyňka": [["Barbora", 2], ["Ctirad", 1], ["Adam", 1], ["Helena", 1], ["Filip", 1], ["Ivan", 2]],
    "Jaroška": [["Ctirad", 2], ["Helena", 2], ["Dana", 1], ["Filip", 2], ["Gabriela", 2], ["Ivan", 1], ["Eva", 1]],
}
STUDENTS_RESULTS_DICT_EMPTY_1 = {
    "Filip": "nezařazen", "Ctirad": "nezařazen", "Dana": "nezařazen", "Eva": "nezařazen", "Ivan": "nezařazen", 
    "Helena": "nezařazen", "Adam": "nezařazen", "Gabriela": "nezařazen", "Barbora": "nezařazen",
}

LOADED_DATA_2 = {
    "Křenka": [["Barbora", 1], ["Adam", 2], ["Gabriela", 1], ["Eva", 2]], 
    "Purkyňka": [["Barbora", 2], ["Ctirad", 1], ["Adam", 1], ["Helena", 1], ["Filip", 1]],
    "Jaroška": [["Ctirad", 2], ["Helena", 2], ["Filip", 2], ["Gabriela", 2], ["Eva", 1]],
}
STUDENTS_RESULTS_DICT_EMPTY_2 = {
    "Filip": "nezařazen", "Ctirad": "nezařazen", "Eva": "nezařazen", "Helena": "nezařazen", "Adam": "nezařazen", 
    "Gabriela": "nezařazen", "Barbora": "nezařazen",
}


@pytest.mark.parametrize(
    ("loaded_data", "students_results_dict_empty"),
    [
        (LOADED_DATA_1, STUDENTS_RESULTS_DICT_EMPTY_1),
        (LOADED_DATA_2, STUDENTS_RESULTS_DICT_EMPTY_2),
    ]
)
def test_get_students_results_dict(loaded_data, students_results_dict_empty):
    students_results_dict = get_students_results_dict(loaded_data)
    assert students_results_dict == students_results_dict_empty
