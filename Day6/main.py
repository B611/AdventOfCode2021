def main():
    with open("input.txt", "r") as infile:
        fishes = [int(i) for i in infile.read().split(",")]

    fish_dict = {}
    for i in range(0, 9):
        fish_dict[i] = fishes.count(i)
    fish_dict["justborn"] = 0
    print("Star 1 :", count_fishes(80, fish_dict))
    print("Star 2 :", count_fishes(256, fish_dict))


def count_fishes(days: int, fish_dict) -> int:
    for i in range(0, days):
        fish_dict["justborn"] += fish_dict[0]
        fish_dict[7] += fish_dict[0]
        fish_dict[0] = 0

        for i2 in range(0, 8):
            fish_dict[i2] += fish_dict[i2 + 1]
            fish_dict[i2 + 1] = 0

        fish_dict[8] += fish_dict["justborn"]
        fish_dict["justborn"] = 0

    return sum(fish_dict.values())


if __name__ == '__main__':
    main()
