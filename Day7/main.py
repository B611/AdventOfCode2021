from typing import List


def main():
    with open("input.txt", "r") as infile:
        positions: List[int] = [int(i) for i in infile.read().split(",")]

    print("Star 1 :", star1(positions))
    print("Star 2 :", star2(positions))


def star1(coords: List[int]) -> int:
    return min([sum([abs(i - x) for x in coords]) for i in range(min(coords), max(coords))])


def star2(coords: List[int]) -> int:
    return min([sum([abs(i - x) * (abs(i - x) + 1) / 2 for x in coords]) for i in range(min(coords), max(coords))])


if __name__ == '__main__':
    main()
