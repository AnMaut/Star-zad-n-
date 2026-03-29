import pytest

from assignment import select_popular_words


@pytest.mark.parametrize(
    ("data", "threshold", "data_popular_expected"),
    [
        ([('máma', 900), ('bába', 800), ('rum', 1024), ('pejsek', 2048)], 1000, [('rum', 1024), ('pejsek', 2048)]),
        ([('máma', 900), ('bába', 800), ('rum', 1024), ('pejsek', 2048)], 800, [('rum', 1024), ('pejsek', 2048), ('máma', 900)]),
        ([('máma', 900), ('bába', 800), ('rum', 1024), ('pejsek', 2048)], None, [('rum', 1024), ('pejsek', 2048)]),
    ]
    )
def test_select_popular_words(data, threshold, data_popular_expected):
    if threshold is None:
        assert set(select_popular_words(data)) == set(data_popular_expected)
    else:
        assert set(select_popular_words(data, threshold)) == set(data_popular_expected)
