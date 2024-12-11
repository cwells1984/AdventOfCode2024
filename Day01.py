def get_input(path):
    list_a = []
    list_b = []
    with open(path, 'r') as f:
        for line in f.readlines():
            line_split = line.strip().split()
            list_a.append(int(line_split[0]))
            list_b.append(int(line_split[1]))
        return list_a, list_b

if __name__ == "__main__":

    list_a, list_b = get_input("Day01_input.txt")

    # Part 1 - sort the list, get the diffs and sum
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    dist = [abs(x-y) for x, y in zip(list_a, list_b)]
    result = sum(dist)
    print(f"Part 1 = {result}")

    # Part 2 - sort the list, get the products, and sum
    list_a, list_b = get_input("Day01_input.txt")

    map_list_b = {}
    for i in list_a:
        map_list_b[i] = 0
    for i in list_b:
        if i in map_list_b:
            map_list_b[i] = map_list_b[i] + 1

    result = 0
    for i in list_a:
        result += i * map_list_b[i]
    print(f"Part 2 = {result}")
