reports = open("d2.in").read().splitlines()

def is_safe(levels):
    diffs = []
    for i in range(1, len(levels)):
        diffs.append(levels[i] - levels[i-1])
    if all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs):
        return True

good_report = 0
good_report_rm_1_level = 0 
for line in reports:
    levels = list(map(int, line.split()))
    if is_safe(levels):
        good_report += 1
    else:
        # brute-force == bad
        for i in range(0, len(levels)):
            new_l = levels[:i] + levels[i+1:]
            if is_safe(new_l):
                good_report_rm_1_level += 1
                break

print(good_report)
print(good_report + good_report_rm_1_level)