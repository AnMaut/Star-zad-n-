SCHOOLS = ["Křenka", "Purkyňka", "Jaroška"]
SCHOOL_MAX_STUDENTS = [3, 2, 2]
NEZARAZEN = "nezařazen"


def load_schools_data_dict(schools_list):
    school_dict = {}
    for school in schools_list:
        with open(f"{school}.csv", "r") as file:
            nam_pref_list = []
            for row in file.readlines()[1:]:
                nm_prf_tuple = row.strip().split(",")
                nm_prf_tuple[1] = int(nm_prf_tuple[1])
                nam_pref_list.append(nm_prf_tuple)

        school_dict[school] = nam_pref_list
    return school_dict

def get_students_results_dict(data_dict):
    names = {}

    for data_list in data_dict.values():
        for name_data in data_list:
            # if name_data[0] not in names:
            names[name_data[0]] = NEZARAZEN

    return names

def remove_student_from_all_schools(schools_data,
                                    studen_name):
    for data in schools_data.values():
        for name_list in data:
            if name_list[0] == studen_name:
                data.remove(name_list)
    return schools_data





# ----------------------------------
# school_dict = {}
#
# for school in SCHOOLS:
#     with open(f"{school}.csv", "r") as file:
#         nam_pref_list = []
#         for row in file.readlines()[1:]:
#             nm_prf_tuple = row.strip().split(",")
#             nam_pref_list.append(nm_prf_tuple)
#             # print(nam_pref_list)
#     school_dict[school] = nam_pref_list
#     # print(school_dict)
#
# names = {}
#
# for data_list in school_dict.values():
#     for name_data in data_list:
#         # if name_data[0] not in names:
#         names[name_data[0]] = NEZARAZEN
# # print(names)
#
# name = "Barbora"
#
# for data in school_dict.values():
#     for name_list in data:
#         if name_list[0] == name:
#             data.remove(name_list)
# print(school_dict)
