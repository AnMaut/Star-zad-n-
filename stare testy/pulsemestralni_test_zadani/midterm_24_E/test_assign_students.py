import pytest
from assignment import assign_students


SCHOOLS = ["Křenka", "Purkyňka", "Jaroška"]
SCHOOL_MAX_STUDENTS = [3, 2, 2]


LOADED_DATA_1 = {
    "Křenka": [["Barbora", 1], ["Adam", 2], ["Dana", 2], ["Gabriela", 1], ["Eva", 2]], 
    "Purkyňka": [["Barbora", 2], ["Ctirad", 1], ["Adam", 1], ["Helena", 1], ["Filip", 1], ["Ivan", 2]],
    "Jaroška": [["Ctirad", 2], ["Helena", 2], ["Dana", 1], ["Filip", 2], ["Gabriela", 2], ["Ivan", 1], ["Eva", 1]],
}
STUDENTS_RESULTS_DICT_EMPTY_1 = {
    "Adam": "nezařazen", "Ivan": "nezařazen", "Helena": "nezařazen", "Barbora": "nezařazen", "Filip": "nezařazen", 
    "Dana": "nezařazen", "Ctirad": "nezařazen", "Eva": "nezařazen", "Gabriela": "nezařazen",
}
CORRECT_STUDENTS_RESULTS_DICT_1 = {
    "Eva": "Křenka", "Barbora": "Křenka", "Helena": "Jaroška", "Ivan": "nezařazen", "Gabriela": "Křenka", 
    "Ctirad": "Purkyňka", "Filip": "nezařazen", "Dana": "Jaroška", "Adam": "Purkyňka",
}
CORRECT_LEFT_PLACES_1 = [0, 0, 0]


@pytest.mark.parametrize(
    ("loaded_data", "students_results_dict_empty", "correct_assignments", "correct_left_places"),
    [
      (LOADED_DATA_1, STUDENTS_RESULTS_DICT_EMPTY_1, CORRECT_STUDENTS_RESULTS_DICT_1, CORRECT_LEFT_PLACES_1),
    ]
)
def test_assign_students(loaded_data, students_results_dict_empty, correct_assignments, correct_left_places):

    students_results_dict, left_places = assign_students(loaded_data, SCHOOLS, SCHOOL_MAX_STUDENTS, students_results_dict_empty)
    assert students_results_dict == correct_assignments
    assert left_places == correct_left_places
