import re


def get_input(path):
    s = ""
    file_ids = []
    current_id = 0
    with open(path, 'r') as f:
        line = list(f.readline().strip())
        for i in range(len(line)):
            if i % 2 == 0:
                s += str(current_id % 10)*int(line[i])
                for j in range(int(line[i])):
                    file_ids.append(current_id)
                current_id += 1
            else:
                s += "."*int(line[i])
                for j in range(int(line[i])):
                    file_ids.append(-1)
        return s, file_ids

def compress_string(s_list, file_ids):
    s_list = list(s)
    free_indexes = []
    num_indexes = []
    for i in range(len(s_list)):
        if s_list[i] == ".":
            free_indexes.append(i)
        else:
            num_indexes.append(i)
    num_indexes.reverse()

    current_num_index = 0
    print("".join(s_list))
    for f in free_indexes:
        n = num_indexes[current_num_index]
        s_list[f] = s_list[n]
        file_ids[f] = file_ids[n]
        s_list[n] = "."
        file_ids[n] = -1
        current_num_index += 1
        if re.match(r"^\d+\.+$", "".join(s_list)):
            break

    return s_list, file_ids


def calc_checksum(file_ids):
    cksum = 0
    for i in range(len(file_ids)):
        if file_ids[i] == -1:
            break
        cksum += i * file_ids[i]
    return cksum


if __name__ == "__main__":

    # Part 1
    s, file_ids = get_input("Day09_Input.txt")
    s_list, file_ids = compress_string(list(s), file_ids)
    cksum = calc_checksum(file_ids)
    print(f"Part 1 Checksum = {cksum}")
