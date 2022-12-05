from enum import Enum


class RoundResult(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

    @classmethod
    def from_str(cls, s: str) -> "RoundResult":
        result_by_str = {
            "X": cls.LOSE,
            "Y": cls.DRAW,
            "Z": cls.WIN,
        }
        return result_by_str[s]

    def score(self) -> int:
        return int(self.value)


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def from_str(cls, s: str) -> "Shape":
        shape_by_str = {
            "A": cls.ROCK,
            "B": cls.PAPER,
            "C": cls.SCISSORS,
            "X": cls.ROCK,
            "Y": cls.PAPER,
            "Z": cls.SCISSORS,
        }
        return shape_by_str[s]

    def shape_score(self) -> int:
        return int(self.value)

    @classmethod
    def round_score(cls, opponent: "Shape", me: "Shape") -> int:
        if opponent == me:
            return 3
        if (
                (opponent == cls.ROCK and me == cls.PAPER) or
                (opponent == cls.PAPER and me == cls.SCISSORS) or
                (opponent == cls.SCISSORS and me == cls.ROCK)
        ):
            return 6
        return 0

    @classmethod
    def deduce_shape(cls, opponent: "Shape", result: RoundResult) -> "Shape":
        if result == RoundResult.DRAW:
            return opponent
        if (
                (opponent == cls.ROCK and result == RoundResult.WIN) or
                (opponent == cls.SCISSORS and result == RoundResult.LOSE)
        ):
            return cls.PAPER
        if (
                (opponent == cls.PAPER and result == RoundResult.WIN) or
                (opponent == cls.ROCK and result == RoundResult.LOSE)
        ):
            return cls.SCISSORS
        return cls.ROCK


score = 0
with open("day2.txt", "r") as f:
    for line in f:
        opponent_shape, my_shape = [Shape.from_str(s) for s in line.strip().split(" ")]
        score += my_shape.shape_score() + Shape.round_score(opponent_shape, my_shape)
print(score)

score = 0
with open("day2.txt", "r") as f:
    for line in f:
        opponent_str, round_str = line.strip().split(" ")
        opponent_shape = Shape.from_str(opponent_str)
        round_result = RoundResult.from_str(round_str)
        my_shape = Shape.deduce_shape(opponent_shape, round_result)
        score += my_shape.shape_score() + round_result.score()
print(score)
