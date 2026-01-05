# https://rosalind.info/problems/iprb/

import sys

intify = lambda x: [int(e) for e in x]
k, m, n = intify(sys.stdin.read().split())


def prob(dom: int, hetero: int, rec: int) -> float:
    # calculate the negative probability, less cases
    # assign probabilities at couple assignment level instead of total_num_punnet_squares
    pop = dom + hetero + rec
    outcomes = pop * (pop - 1) / 2
    hhprobneg = hetero * (hetero - 1) / 2 * 0.25
    hrprobneg = hetero * rec * 0.5
    rrprobneg = rec * (rec - 1) / 2
    negprob = 1 - (hrprobneg + hhprobneg + rrprobneg) / outcomes
    return negprob


print(prob(k, m, n))
