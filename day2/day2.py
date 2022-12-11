# A, X = ROCK
# B, Y = PAPER
# C, Z = SCISSOR
HAND_POINTS = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

GAME_POINTS = {
    'LOSS': 0,
    'DRAW': 3,
    'WIN': 6
}

ROUND_POINTS = {
    'A X': 'DRAW',
    'A Y': 'WIN',
    'A Z': 'LOSS',
    'B X': 'LOSS',
    'B Y': 'DRAW',
    'B Z': 'WIN',
    'C X': 'WIN',
    'C Y': 'LOSS',
    'C Z': 'DRAW'
}

TROLL_HAND_POINTS = {
    'A': 1,
    'B': 2,
    'C': 3,
}

TROLL_GAME_POINTS = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

MY_HAND_POINTS = {
    'A X': 3,
    'A Y': 1,
    'A Z': 2,
    'B X': 1,
    'B Y': 2,
    'B Z': 3,
    'C X': 2,
    'C Y': 3,
    'C Z': 1
}


def get_score(strategy_guide):
    total_score = 0
    troll_total_score = 0
    for round in strategy_guide:
        round_score = HAND_POINTS[round[-1]] + GAME_POINTS[ROUND_POINTS[round]]
        troll_round_score = MY_HAND_POINTS[round] + \
            TROLL_GAME_POINTS[round[-1]]
        total_score += round_score
        troll_total_score += troll_round_score
    return [total_score, troll_total_score]


def get_lines(input_file_string):
    with open(input_file_string, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        strategy_guide = [line.strip() for line in lines]
        return (get_score(strategy_guide))


print(get_lines('input1.txt'))
print(get_lines('input2.txt'))
