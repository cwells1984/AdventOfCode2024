import re

def get_input(path):
    mults = []
    with open(path, 'r') as f:
        for line in f.readlines():
            mults.append(line.strip())
    return mults

if __name__ == "__main__":
    # Part 1
    mults = get_input("Day03_Input.txt")
    all_results = 0
    for mult in mults:
        result = 0
        for mul_command in re.findall(r"mul\(\d+,\d+\)", mult):
            mul_nums = re.findall(r"\d+", mul_command)
            result += int(mul_nums[0]) * int(mul_nums[1])
        all_results += result
    print(f"Part 1 All Results = {all_results}")

    # Part 2
    mults = get_input("Day03_Input.txt")
    all_results = 0
    ins_enabled = True
    for mult in mults:
        mult_splits = re.findall(r"(do\(\)|don\'t\(\)|mul\(\d+,\d+\))", mult)
        result = 0
        for mult_split in mult_splits:
            if mult_split == "do()":
                ins_enabled = True
            elif mult_split == "don\'t()":
                ins_enabled = False
            elif ins_enabled:
                mul_nums = re.findall(r"\d+", mult_split)
                result += int(mul_nums[0]) * int(mul_nums[1])
        all_results += result
    print(f"Part 2 All Results = {all_results}")