from typing import List
from BingoCard import BingoCard


def main():
    lines: List[str] = parse_input()
    draw_list: List[int] = [int(i) for i in lines[0].split(",")]
    cards: List[BingoCard] = []
    card_data: List[List[int]] = []

    for line in lines[2:]:
        if line and line != "\n":
            card_data.append([int(i) for i in line.split(" ")])
        else:
            cards.append(BingoCard(card_data))
            card_data = []
    cards.append(BingoCard(card_data))

    print("Star 1 :", get_winning_board(draw_list, cards))
    print("Star 2 :", get_losing_board(draw_list, cards))


def get_winning_board(draw_list: List[int], cards: List[BingoCard]) -> int:
    for draw in draw_list:
        for card in cards:
            card.check_draw(draw)
            if card.check_bingo():
                return card.compute_score() * draw


def get_losing_board(draw_list: List[int], cards: List[BingoCard]) -> int:
    last_compute = 0

    for draw in draw_list:
        for card in cards:
            card.check_draw(draw)
            if card.check_bingo() and not card.won:
                if len(cards) > 1:
                    last_compute = card.compute_score() * draw
                    card.won = True
                else:
                    return last_compute
    return last_compute


def parse_input() -> List[str]:
    with open("input.txt", "r") as input_file:
        lines: List[str] = input_file.readlines()
        for i in range(0, len(lines)):
            if lines[i].startswith(" "):
                lines[i] = lines[i][1:]
            lines[i] = lines[i].replace("  ", " ")
            lines[i] = lines[i].replace("\n", "")
    return lines


if __name__ == '__main__':
    main()
