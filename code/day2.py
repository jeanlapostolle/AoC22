strat = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

game = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}

strat2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
game2 = {
    'A X': 3,
    'A Y': 1,
    'A Z': 2,
    'B X': 1,
    'B Y': 2,
    'B Z': 3,
    'C X': 2,
    'C Y': 3,
    'C Z': 1,
}


def compute(inputPath):
    with open(inputPath, "r") as f:
        line = f.readline().strip()
        score = 0
        while line:
            score += strat[line[2]]
            score += game[line]
            line = f.readline().strip()
        return score


def compute_2(inputPath):
    with open(inputPath, "r") as f:
        line = f.readline().strip()
        score2 = 0
        while line:
            score2 += strat2[line[2]]
            score2 += game2[line]
            line = f.readline().strip()
        return score2


