import pytest

from assignment import get_words_with_letter_restriction


@pytest.mark.parametrize(
    ("data", "letters", "data_letters_expected"),
    [
        ([('máma', 900), ('bába', 800), ('rum', 1024), ('pejsek', 2048)], ["m", "a", "á", "o", "ó", "b"], [('máma', 900), ('bába', 800)]),
        ([('máma', 900), ('bába', 800), ('rum', 1024), ('pejsek', 2048)], ["m", "a", "á", "o", "ó", "b", "p"], [('máma', 900), ('bába', 800)]),
        ([('máma', 900), ('bába', 800), ('rum', 1024), ('pejsek', 2048)], ["m", "a", "á", "o", "ó"], [('máma', 900),]),
        ([('máma', 900), ('bába', 800), ('rum', 1024), ('pejsek', 2048)], ["m", "a", "á", "o", "ó", "p", "e", "j", "s", "k"], [('máma', 900), ('pejsek', 2048)]),
    ]
    )
def test_get_words_with_letter_restriction(data, letters, data_letters_expected):
    assert set(get_words_with_letter_restriction(data, letters)) == set(data_letters_expected)

