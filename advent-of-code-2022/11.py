from dataclasses import dataclass
from typing import List
import re

lines = open("11.in").read().splitlines()


@dataclass
class Monkey:
    index: int
    items: List[int]
    operation_operator: str
    operation_operand: int
    divisor: int
    monkey_on_true: int
    monkey_on_false: int
    total_inspected: int = 0
    worry_divisor: int = 3

    def operation(self, old):
        oper = None
        if self.operation_operand == "old":
            oper = old
        else:
            oper = int(self.operation_operand)

        if self.operation_operator == "*":
            return old * oper
        elif self.operation_operator == "+":
            return old + oper

    def turn(self, monk_dict, mod=None):
        for item in self.items:
            worry = self.operation(item) // self.worry_divisor
            if mod:
                worry = worry % mod
            monk = self.monkey_on_false
            if worry % self.divisor == 0:
                monk = self.monkey_on_true
            monk_dict[monk].items.append(worry)
            self.total_inspected += 1
        self.items = []

    @classmethod
    def from_text(cls, lines):
        i = 0
        monkey_idx = int(re.search("Monkey (\d+):", lines[i]).group(1))
        starting_items = (
            re.search("Starting items: (.*)", lines[i + 1]).group(1).split(", ")
        )
        starting_items = list(map(int, starting_items))
        operation = re.search("new = old ([+*]) (.*)", lines[i + 2])
        operator = operation.group(1)
        operand = operation.group(2)
        test_divisor = int(re.search("divisible by (\d+)", lines[i + 3]).group(1))
        truth_throw = int(re.search("throw to monkey (\d+)", lines[i + 4]).group(1))
        false_throw = int(re.search("throw to monkey (\d+)", lines[i + 5]).group(1))
        return cls(
            index=monkey_idx,
            items=starting_items,
            operation_operator=operator,
            operation_operand=operand,
            divisor=test_divisor,
            monkey_on_true=truth_throw,
            monkey_on_false=false_throw,
        )


monkeys = dict()
for i in range(0, len(lines), 7):
    monkey = Monkey.from_text(lines[i : i + 7])
    monkeys[monkey.index] = monkey

for i in range(20):
    for monk_idx in sorted(monkeys):
        monkeys[monk_idx].turn(monkeys)

ordered = sorted([monk.total_inspected for monk in monkeys.values()])
print(ordered)
print(ordered[-1] * ordered[-2])

monkeys = dict()
for i in range(0, len(lines), 7):
    monkey = Monkey.from_text(lines[i : i + 7])
    monkey.worry_divisor = 1
    monkeys[monkey.index] = monkey

all_primes = 1
for m in monkeys.values():
    all_primes *= m.divisor
monk_idxs = sorted(monkeys.keys())
print(monk_idxs)
for i in range(10000):
    if i % 1000 == 0:
        print(i)
    for monk_idx in monk_idxs:
        monkeys[monk_idx].turn(monkeys, mod=all_primes)
ordered = sorted([monk.total_inspected for monk in monkeys.values()])
print(ordered)
print(ordered[-1] * ordered[-2])
# BAD : 10732285959
# BAD : 8886450348
