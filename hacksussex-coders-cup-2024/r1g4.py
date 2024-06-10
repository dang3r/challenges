import pytest


def solve(rectangles: list[list[int]]) -> int:
    lengths = [min(rectangle) for rectangle in rectangles]
    largest = max(lengths)
    satisfying = [length for length in lengths if length == largest]
    return len(satisfying)


test_cases = [([[5, 8], [5, 7], [1, 3], [5, 10]], 3)]


@pytest.mark.parametrize("rectangles,answer", test_cases)
def test_solve(rectangles, answer):
    assert solve(rectangles) == answer
