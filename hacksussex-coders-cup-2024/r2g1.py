import pytest


def solve(a, b, c) -> int:
    points = 0
    while len([d for d in [a, b, c] if d > 0]) >= 2:
        a, b, c = sorted([a, b, c])
        points += 1
        c -= 1
        b -= 1
    return points


test_cases = [([2, 4, 6], 6), ([1, 3, 5], 4), ((0, 1, 2), 1)]


@pytest.mark.parametrize("nums,answer", test_cases)
def test_solve(nums, answer):
    assert solve(*nums) == answer
