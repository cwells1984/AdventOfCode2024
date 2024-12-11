def get_input(path):
    reports = []
    with open(path, 'r') as f:
        for line in f.readlines():
            line_split = line.strip().split()
            report = []
            for i in line.strip().split():
                report.append(int(i))
            reports.append(report)
        return reports

def get_report_diffs(report):
    return [report[i] - report[i-1] for i in range(1, len(report))]

def check_report_safety(diffs):
    is_safe = True
    if diffs[0] < 0:
        expect_negative = True
    else:
        expect_negative = False

    # Now check the diffs
    for diff in diffs:
        diff_ab = abs(diff)

        # If the difference <0 and we expect positive, we fail
        if diff < 0 and not expect_negative:
            is_safe = False
            return is_safe
        # Otherwise, if the difference is >0 and we expect negative, we fail
        elif diff > 0 and expect_negative:
            is_safe = False
            return is_safe
        # Otherwise, if the difference is not between 1 and 3, we fail
        elif not 1 <= diff_ab <= 3:
            is_safe = False
            return is_safe

    return is_safe

def check_report_safety_part2(report):

    # Check all of the possible combinations of this report with one level missing
    # If any are safe the report is safe
    for i in range(0, len(report)):
        smaller_report = report[0:i] + report[i+1:]
        diffs = get_report_diffs(smaller_report)
        if check_report_safety(diffs):
            return True
    return False


if __name__ == "__main__":
    reports = get_input("Day02_Input.txt")

    # Part 1
    num_safe = 0
    for report in reports:
        if check_report_safety(get_report_diffs(report)):
            num_safe += 1
    print(f"Part 1 # Safe Reports = {num_safe}")

    # Part 2, allow one bad level
    num_safe = 0
    for report in reports:
        if check_report_safety_part2(report):
            num_safe += 1
    print(f"Part 2 # Safe Reports = {num_safe}")
