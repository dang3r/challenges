
nums = list(map(int, open("d1.in").readlines()))
target = 2020
s = set()

for num in nums:
    if target - num in s:
        print(num * (target - num))
        break
    s.add(num)


d = dict()
for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        d[nums[i] + nums[j]] = (nums[i], nums[j])

for num in nums:
    if target - num in d:
        print(num * d[target - num][0] * d[target - num][1])
        break

