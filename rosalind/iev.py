import sys

# https://rosalind.info/problems/iev/

line = sys.stdin.read()
nums = [int(val) for val in line.split()]

d = {
    "AA-AA": 1,
    "AA-Aa": 1,
    "AA-aa": 1,
    "Aa-Aa": 0.75,
    "Aa-aa": 0.5,
    "aa-aa": 0.0
}
probs = list(d.values())
print(sum(nums[i]* probs[i]*2 for i in range(len(nums))))


