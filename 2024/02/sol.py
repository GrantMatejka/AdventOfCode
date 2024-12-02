ex = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

with open("input.txt") as f:
    # src = ex.strip().split("\n")
    src = f.read().split("\n\n")[0].split("\n")

    reports = [[int(n) for n in line.split()] for line in src]

    total = 0
    for report in reports:
        safe = True
        increasing = report[0] < report[1]
        for i in range(1, len(report)):
            difference = report[i] - report[i-1]
            still_increasing = difference > 0
            safe_difference = 1 <= abs(difference) <= 3
            if not safe_difference or increasing != still_increasing:
                safe = False
        if safe:
            total += 1

    print(total)

with open("input.txt") as f:
    # src = ex.strip().split("\n")
    src = f.read().split("\n\n")[0].split("\n")

    reports = [[int(n) for n in line.split()] for line in src]

    total = 0
    for report in reports:
        report_mutations = []
        for i in range(len(report)):
            report_mutations.append(report[:i] + report[i+1:])
        any_safe = False
        for report in report_mutations:
            safe = True
            increasing = report[0] < report[1]
            for i in range(1, len(report)):
                difference = report[i] - report[i-1]
                still_increasing = difference > 0
                safe_difference = 1 <= abs(difference) <= 3
                if not safe_difference or increasing != still_increasing:
                    safe = False
            if safe:
                any_safe = True
                break
        if any_safe:
            total += 1

    print(total)