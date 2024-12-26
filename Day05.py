from functools import cmp_to_key

import re

def get_inputs(path):
    rules = {}
    s_list = []
    reading_rules = True
    with open(path, 'r') as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                reading_rules = False
                continue
            if reading_rules:
                line_split = line.strip().split("|")
                before_num = int(line_split[0])
                after_num = int(line_split[1])

                # Add the before -> after rule
                if before_num not in rules:
                    rules[before_num] = [after_num]
                else:
                    rules[before_num].append(after_num)
            else:
                s_list.append(line.strip())
        return rules, s_list

def is_order_valid(s, rules):
    s_nums = [int(i) for i in s.split(",")]
    for i in range(len(s_nums)):
        s_num = s_nums[i]
        prec_nums = s_nums[0:i]
        if s_num in rules:
            for j in rules[s_num]:
                if j in prec_nums:
                    # print(f"{s_num} failed, caught {j} before it!")
                    return False
        # print(f"{s_num} succeeded!")
    # print(f"{s} obeys the rule!")
    return True


def find_middle_page_number(s):
    s_nums = [int(i) for i in s.split(",")]
    mid_index = len(s_nums) // 2
    return s_nums[mid_index]


def custom_cmp(x, y):
    if x in g_rules:
        after_x = g_rules[x]
    else:
        after_x = []
    if y in g_rules:
        after_y = g_rules[y]
    else:
        after_y = []

    # If y should be after x, 0
    if y in after_x:
        return -1
    # If x should be after y, -1
    elif x in after_y:
        return 1
    # Otherwise 0
    else:
        return 0


if __name__ == "__main__":

    # Part 1 get the sum of middle pages for well-formed strings
    rules, s_list = get_inputs("Day05_input.txt")
    middle_page_sum = 0
    for s in s_list:
        if is_order_valid(s, rules):
            middle_page_sum += find_middle_page_number(s)
            # print(f"{find_middle_page_number(s)}")
    print(f"Part 1 - middle page sum = {middle_page_sum}")

    # Part 2 fet the sum of middle pages from corrected strings
    global g_rules
    g_rules, s_list = get_inputs("Day05_input.txt")
    middle_page_sum = 0
    for s in s_list:
        if not is_order_valid(s, g_rules):
            s_nums = [int(i) for i in s.split(",")]
            rearranged_s_nums = sorted(s_nums, key=cmp_to_key(custom_cmp))
            mid_index = len(rearranged_s_nums) // 2
            middle_page_sum += rearranged_s_nums[mid_index]
    print(f"Part 2 - middle page sum = {middle_page_sum}")
