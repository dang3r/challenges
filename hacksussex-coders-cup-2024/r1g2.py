import pytest


def solve(matrix) -> bool:
    n = len(matrix)
    god = set(range(1, n + 1))
    for i in range(n):
        column = set(matrix[i][j] for j in range(n))
        row = set(matrix[i])
        if row != god or column != god:
            return False

    return True


test_cases = [
    ([[1, 2, 3], [2, 3, 1], [3, 1, 2]], True),
    ([[1, 2, 3], [2, 3, 1], [3, 1, 1]], False),
]


@pytest.mark.parametrize("matrix,answer", test_cases)
def test_solve(matrix, answer):
    assert solve(matrix) == answer
