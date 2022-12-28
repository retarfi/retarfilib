from typing import List

import pytest

from retarfilib.mecabsplit import get_tango


@pytest.mark.parametrize(
    "sentence, expected",
    [
        (
            "未来科学部でコンビニ店員になりきってお釣りを返していこう！",
            ["未来科学部", "コンビニ店", "員", "なる", "きる", "お釣り", "返す", "いく"],
        ),
    ],
)
def test_get_tango(sentence: str, expected: List[str]) -> None:
    assert get_tango(sentence) == expected
