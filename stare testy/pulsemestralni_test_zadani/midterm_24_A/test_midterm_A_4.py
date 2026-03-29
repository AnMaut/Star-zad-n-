import pytest
from midterm_A import main


@pytest.mark.parametrize(
    ("dna_list", "expected_results"),
    [
        (
            ["MTZAMTAMTA"],
            [(9, 'jablko', 'Pokemon se uzdravil bez mutace')]
        ),
        (
            ["MMMMMT", "MTZAMTAMTA"],
            [(3, 'prasky', 'Pokemon se vyvinul na jeho dalsi level'), (9, 'jablko', 'Pokemon se uzdravil bez mutace')]
        ),
        (
            ["ZMZMZMZMZMAA", "MTZAMTAMTA", "MTZAM", "AATTAATTAZZTTTTTTTT"],
            [
                (9, 'jablko', 'Pokemon se uzdravil bez mutace'),
                (9, 'jablko', 'Pokemon se uzdravil bez mutace'),
                (9, 'prasky', 'Pokemon se uzdravil, ale nema dostatecnou energii se vyvinout'),
                (3, 'injekce', 'Pokemon se vyvinul na jeho dalsi level'),
            ],
         ),
    ]
)
def test_main(dna_list, expected_results):
    assert main(dna_list) == expected_results
