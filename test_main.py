import pytest

from main import Solution


@pytest.mark.parametrize(
    "case,res",
    [
        (
            [],
            None,
        ),
    ],
)
def test_cases(case, res):
    # Change the name of `method` below
    assert Solution().method(*case) == res
