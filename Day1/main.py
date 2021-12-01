from typing import List


def main():
    with open("input.txt", "r") as input_file:
        lines: List[int] = [int(line) for line in input_file]

    print("Star 1 :", count_inc(lines))
    print("Star 2 :", count_inc_window(lines, 3))


def count_inc(data: List[int]) -> int:
    return sum(data[i] > data[i - 1] for i in range(1, len(data)))


def count_inc_window(data: List[int], size: int) -> int:
    return sum(sum(data[i: i + size]) > sum(data[i - 1: i + size - 1]) for i in range(0, len(data) - size))


if __name__ == '__main__':
    main()
