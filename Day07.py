from enum import Enum
from itertools import product
import re

class Operations(Enum):
    ADD = "+"
    MULT = "*"

def get_input(path):
    equations = []
    with open(path, 'r') as f:
        for line in f.readlines():
            nums = re.findall(r"\d+", line.strip())
            total = int(nums[0])
            eq_nums = []
            for num in nums[1:]:
                eq_nums.append(int(num))
            equations.append([total, eq_nums])
        return equations

def match_equation(equation):

    # Get the total, nums, and calculate a list of all permutations of ops
    real_total = equation[0]
    nums = equation[1]
    operation_attempts = list(product(operations, repeat=len(nums) - 1))

    # Now for each operation calculate the total
    for operation_attempt in operation_attempts:
        total = nums[0]
        for i in range(len(operation_attempt)):
            if operation_attempt[i] == Operations.ADD:
                total += nums[i + 1]
            elif operation_attempt[i] == Operations.MULT:
                total *= nums[i + 1]
        if real_total == total:
            return real_total
    return 0

if __name__ == "__main__":
    equations = get_input("Day07_Input.txt")
    operations = [Operations.ADD, Operations.MULT]
    result = 0
    for equation in equations:
        result += match_equation(equation)
    print(f"Part 1 Result {result}")
