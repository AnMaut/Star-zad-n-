
FREEZERS_THRESHOLDS = [
    ('small1', -15),
    ('small2', -16),
    ('large1', -20),
    ('large2', -21),
    ('cells1', -60),
    ('sample', -55),
    ('lowtem', -120),
    ('zmrzka', -15),
    ]



# def main(sensors_stream, freezers_names):
#     error_names_all = []
#     high_temp_names_all = []
#
#     is_error_list_last = [False] * len(freezers_names)
#     is_above_threshold_list_last = [False] * len(freezers_names)
#     for measurement_timepoint in sensors_stream:
#
#         measurement_timepoint_fix = fix_names(measurement_timepoint, freezers_names)
#         measurement_timepoint_ordered = order(measurement_timepoint_fix, freezers_names)
#         is_error_list, is_above_threshold_list = check_if_above_threshold(measurement_timepoint_ordered)
#         error_names, high_temp_names = get_alarm_decision(is_error_list, is_error_list_last, is_above_threshold_list, is_above_threshold_list_last, freezers_names)
#
#         if error_names:
#             print(f'Error of freezers: {error_names}')
#         if high_temp_names:
#             print(f'High temperature of freezers: {high_temp_names}')
#
#         is_error_list_last = is_error_list
#         is_above_threshold_list_last = is_above_threshold_list
#
#         error_names_all.append(error_names)
#         high_temp_names_all.append(high_temp_names)
#
#     return error_names_all, high_temp_names_all


if __name__ == '__main__':

    sensors_stream = [
        [('small1', -20.1), ('zmrwka', -16.2), ('large1', None), ('cells1', -62.2), ],
        [('lawge1', -21.8), ('small1', -19.7), ('zmrzka', -12.6), ('small2', -22.7), ('cells1', -63.5), ],
        [('zmrzka', -11.3), ('celws1', -65.1), ('large1', None), ('smggl1', -17.2), ],
        [('laree1', None), ('small1', -22.8), ('zmrjka', -10.3), ('cllls1', -66.3), ],
    ]
    freezers_names = ['small1', 'small2', 'zmrzka', 'large1', 'cells1']

    # error_names_all, high_temp_names_all = main(sensors_stream, freezers_names)
    # print(error_names_all, high_temp_names_all)
