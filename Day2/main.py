from typing import List, Tuple


def main():
    with open("input.txt", "r") as input_file:
        values = [(line.split(" ")[0], int(line.split(" ")[1]),) for line in input_file]
    print("Star 1 :", calc_position(values))
    print("Star 2 :", calc_position_aim(values))


def calc_position(values: List[Tuple[str, int]]) -> int:
    return sum([v[1] if v[0] == "down" else -v[1] if v[0] == "up" else 0 for v in values]) * sum(
        [v[1] if v[0] == "forward" else 0 for v in values])


def calc_position_aim(values: List[Tuple[str, int]]) -> int:
    x, y, aim = 0, 0, 0

    for v in values:
        aim += v[1] if v[0] == "down" else -v[1] if v[0] == "up" else 0
        x += v[1] if v[0] == "forward" else 0
        y += v[1] * aim if v[0] == "forward" else 0

    return x * y


if __name__ == '__main__':
    main()
