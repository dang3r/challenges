# https://rosalind.info/problems/iprb/
#
#

import sys

intify = lambda x: [int(e) for e in x]
k, m, n = 2, 2, 2
k, m, n = intify(sys.stdin.read().split())


def prob(dom, hetero, rec):
    # 0 - prob(at least 1 dominant allele)
    pop = dom + hetero + rec
    outcomes = (pop * (pop - 1) / 2) * 4
    dprob = (dom * (dom - 1) / 2) * 4
    dhprob = (dom * hetero) * 4
    drprob = (dom * rec) * 4
    hhprob = (hetero * (hetero - 1) / 2) * 3
    hrprob = hetero * rec * 2
    posprob = sum([dprob, dhprob, drprob, hhprob, hrprob]) / outcomes

    # 1 - prob(all recessive alleles)
    hhprobneg = hetero * (hetero - 1) / 2 * 1
    hrprobneg = hetero * rec * 2
    rrprobneg = rec * (rec - 1) / 2 * 4
    negprob = 1 - ((hrprobneg + hhprobneg + rrprobneg) / outcomes)

    return posprob


print(prob(k, m, n))
