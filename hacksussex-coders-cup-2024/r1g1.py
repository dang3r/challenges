import pytest

"""
Destination city.

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
"""


def solve_firstpass(paths: list[list[str]]) -> str:
    srcs = set()
    dsts = set()
    for src, dst in paths:
        srcs.add(src)
        dsts.add(dst)

    final = dsts - srcs
    assert len(final) == 1
    return list(final)[0]


def solve_elegant(paths: list[list[str]]) -> str:
    srcs, dsts = zip(*paths)
    final = set(dsts) - set(srcs)
    return list(final)[0]


tests = [([["a", "b"]], "b"), ([["c", "d"], ["d", "e"]], "e")]


@pytest.mark.parametrize("func", [solve_firstpass, solve_elegant])
@pytest.mark.parametrize("paths,answer", tests)
def test_solve(func, paths, answer):
    assert func(paths) == answer
