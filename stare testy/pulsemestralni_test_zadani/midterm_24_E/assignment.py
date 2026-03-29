SCHOOLS = ["Křenka", "Purkyňka", "Jaroška"]
SCHOOL_MAX_STUDENTS = [3, 2, 2]
NEZARAZEN = "nezařazen"


def load_schools_data_dict(schools_list):
    school_dict = {}
    for school in SCHOOLS:
        with open(f"{school}.csv", "r") as file:
            nam_pref_list = []
            for row in file.readlines()[1:]:
                nm_prf_tuple = row.strip().split(",")
                nam_pref_list.append(tuple(nm_prf_tuple))

        school_dict[school] = nam_pref_list



# ----------------------------------
# school_dict = {}
#
# for school in SCHOOLS:
#     with open(f"{school}.csv", "r") as file:
#         nam_pref_list = []
#         for row in file.readlines()[1:]:
#             nm_prf_tuple = row.strip().split(",")
#             nam_pref_list.append(tuple(nm_prf_tuple))
#             print(nam_pref_list)
#     school_dict[school] = nam_pref_list
#     print(school_dict)








