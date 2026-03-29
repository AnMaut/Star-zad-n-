import pytest
from assignment import load_schools_data_dict


SCHOOLS = ["Křenka", "Purkyňka", "Jaroška"]
SCHOOL_MAX_STUDENTS = [3, 2, 2]


KRENKA = [["Barbora", 1], ["Adam", 2], ["Dana", 2], ["Gabriela", 1], ["Eva", 2]]
PURKYNKA = [["Barbora", 2], ["Ctirad", 1], ["Adam", 1], ["Helena", 1], ["Filip", 1], ["Ivan", 2]]
JAROSKA = [["Ctirad", 2], ["Helena", 2], ["Dana", 1], ["Filip", 2], ["Gabriela", 2], ["Ivan", 1], ["Eva", 1]]


@pytest.mark.parametrize(
    ("schools_names", "correct_loaded_data"),
    [
        (SCHOOLS[:2], {"Křenka": KRENKA, "Purkyňka": PURKYNKA}),
        (SCHOOLS, {"Křenka": KRENKA, "Purkyňka": PURKYNKA, "Jaroška": JAROSKA}),
    ]
)
def test_load_schools_data_dict(schools_names, correct_loaded_data):
    loaded_data = load_schools_data_dict(schools_names)
    assert loaded_data == correct_loaded_data
