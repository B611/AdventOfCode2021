from typing import List


def main():
    with open("input.txt", "r") as input_file:
        lines: List[str] = input_file.read().split("\n")

    print("Star 1 :", get_gamma_times_epsilon(lines))
    print("Star 2 :", get_o2_times_co2(lines))


def get_gamma_times_epsilon(lines: List[str]) -> int:
    gamma: List[str] = []
    epsilon: List[str] = []

    for i in range(0, len(lines[0]) - 1):
        nums = [lines[i2][i] for i2 in range(len(lines))]
        gamma.append("1" if nums.count("1") > nums.count("0") else "0")
        epsilon.append("0" if nums.count("1") > nums.count("0") else "1")

    return int("".join(gamma), 2) * int("".join(epsilon), 2)


def get_o2_times_co2(lines: List[str]) -> int:
    return get_value(lines, True) * get_value(lines, False)


def get_value(data, common) -> int:
    for i in range(len(data[0])):
        col = list(map(list, zip(*data)))[i]
        tokeep = int(col.count("1") >= col.count("0")) if common else int(col.count("1") < col.count("0"))
        newlist = []

        for i2 in range(0, len(data)):
            if int(data[i2][i]) == tokeep:
                newlist.append(data[i2])
        data = newlist
        if len(data) == 1:
            return int("".join(data[0]), 2)


if __name__ == '__main__':
    main()
