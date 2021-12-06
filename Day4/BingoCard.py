from typing import List


class BingoCard:
    def __init__(self, lines):
        self.lines: List[List[int]] = lines
        self.matches: List[List[bool]] = [[False for i in range(len(lines[0]))] for j in range(len(lines))]
        self.score: int = 0
        self.won: bool = False

    def check_draw(self, draw: int) -> None:
        for y in range(0, len(self.lines)):
            for x in range(0, len(self.lines[y])):
                if not self.matches[y][x] and draw == self.lines[y][x]:
                    self.matches[y][x] = True

    def check_bingo(self) -> bool:
        for line in self.matches:
            if False not in line:
                return True

        for column in list(map(list, zip(*self.matches))):
            if False not in column:
                return True

        return False

    def compute_score(self) -> int:
        for y in range(0, len(self.matches)):
            for x in range(0, len(self.matches[y])):
                if not self.matches[y][x]:
                    self.score += self.lines[y][x]
        return self.score
