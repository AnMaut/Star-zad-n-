from assignment import main


def test_main_1():

    file_name = "words.csv"
    threshold = 1000
    letters = ["m", "a", "á", "o", "ó", "b", "c", "j", "e", "i"]
    template = ["xoxo"]
    
    expected = [('moci', 1237805), ('mimo', 61472), ('máma', 41480), ('jáma', 5947), ('mimi', 3861), ('bába', 2505), ('bobo', 2197), ('baba', 1540), ('babi', 1376)]

    assert set(main(file_name, threshold, letters, template)) == set(expected)


def test_main_2():

    file_name = "words.csv"
    threshold = 800
    letters = ["m", "a", "á", "o", "ó", "b", "c", "j", "e", "i"]
    template = ["xoxo", "xoxox"]
    
    expected = [('moci', 1237805), ('mimo', 61472), ('máma', 41480), ('jáma', 5947), ('mimi', 3861), ('bába', 2505), ('bobo', 2197), ('baba', 1540), ('babi', 1376), ('jojo', 938), ('jacob', 1501)]

    assert set(main(file_name, threshold, letters, template)) == set(expected)


def test_main_3():

    file_name = "words.csv"
    threshold = 1000
    letters = ["m", "a", "á", "o", "ó", "b", "c", "j", "e", "i"]
    template = ["xoxoxoxo"]
    
    expected = "Nebyla nalezena žádná slova pro zadané podmínky."

    assert main(file_name, threshold, letters, template) == expected
