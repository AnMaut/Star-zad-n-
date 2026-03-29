from assignment import read_words_data


def test_read_words_data():
    
    file_path = "words_small.csv"
    expected_data = [('máma', 900), ('bába', 800), ('rum', 1024), ('pejsek', 2048)]

    assert read_words_data(file_path) == expected_data
