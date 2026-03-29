import pytest

from assignment import get_words_by_template

X = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
     'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
O = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']


@pytest.mark.parametrize(
    ("data", "template", "data_template_expected"),
    [
        ([('máma', 900), ('bába', 800), ('rum', 1024), ('pejsek', 2048)], "xox", [('rum', 1024)]),
        ([('máma', 900), ('bába', 800), ('rum', 1024), ('pejsek', 2048)], "xoxo", [('máma', 900), ('bába', 800)]),
    ]
    )
def test_get_words_by_template(data, template, data_template_expected):
    assert set(get_words_by_template(data, template)) == set(data_template_expected)
    