import pytest


def solve(s1, s2) -> bool:
    s1 = list(s1)
    s2 = list(s2)
    if len(s1) != len(s2):
        return False

    diff_idxs = [i for i in range(len(s1)) if s1[i] != s2[i]]

    if len(diff_idxs) == 0:
        return True
    elif len(diff_idxs) == 2:
        i, j = diff_idxs
        s1[i], s1[j] = s1[j], s1[i]
        return s1 == s2
    return False


test_cases = [
    (["abcdef", "abcdef"], True),
    (["abc", "abcdef"], False),
    (["abc", "cba"], True),
    (["abcde", "abcdf"], False),
    (["", ""], True),  # Empty strings should return True
    (["a", "a"], True),  # Single character strings should return True
    (["abc", "abc"], True),  # Identical strings should return True
    (["abc", "acb"], True),  # Strings with two character swaps should return True
    (["abc", "bac"], True),  # Strings with two character swaps should return true
    (["abc", "abcd"], False),  # Strings with different lengths should return False
]


@pytest.mark.parametrize("strings,answer", test_cases)
def test_solve(strings, answer):
    assert solve(*strings) == answer
