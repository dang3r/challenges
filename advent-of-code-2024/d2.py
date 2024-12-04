reports = open("d2.in").read().splitlines()

def original_solution():
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

def revised_solution():
    # ideas taken from https://www.youtube.com/watch?v=4NRODX4skCM
    # key ones:
    #   - instead of building the diffs, use the zip trick of zip(a, a[1:]) to compare two adjacent elements
    #   - use any() when determining if any level after a single removal is good
    def is_safe(level: list[int]) -> bool:
        asc = all(a > b for a,b in zip(level, level[1:]))
        desc = all(a < b for a,b in zip(level, level[1:]))

        if not (asc or desc):
            return False

        level = sorted(level)
        return all(1 <= (b-a) <=3 for a,b in zip(level, level[1:]))

    reports = open("d2.in").read().splitlines()

    p1_good = 0
    p2_good = 0
    for line in reports:
        level = list(map(int, line.split()))
        if is_safe(level):
            p1_good +=1
            p2_good += 1
        else:
            good_after_removal = any(is_safe(level[:i] + level[i+1:]) for i in range(len(level)))
            if good_after_removal:
                p2_good +=1

        

    print(p1_good)
    print(p2_good)

original_solution()
revised_solution()

    
