data = open("06.in").read().strip()
for i in range(0, len(data) - 4):
    if len(set(data[i : i + 4])) == 4:
        break
print(i + 4)

for i in range(0, len(data) - 14):
    if len(set(data[i : i + 14])) == 14:
        break
print(i + 14)
