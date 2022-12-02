# --- Part Two ---
# The Elf finishes helping with the tent and sneaks back 
# over to you. "Anyway, the second column says how the 
# round needs to end: X means you need to lose, Y means 
# you need to end the round in a draw, and Z means you 
# need to win. Good luck!"

# The total score is still calculated in the same way, 
# but now you need to figure out what shape to choose so 
# the round ends as indicated. The example above now 
# goes like this:

# In the first round, your opponent will choose Rock (A), 
# and you need the round to end in a draw (Y), so you also 
# choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), 
# and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors 
# with Rock for a score of 1 + 6 = 7.
# Now that you're correctly decrypting the ultra top secret 
# strategy guide, you would get a total score of 12.

# Following the Elf's instructions for the second column, what 
# would your total score be if everything goes exactly according 
# to your strategy guide?

# Your puzzle answer was 10398.

with open("day-2/input.txt", mode = "r", encoding = "UTF-8") as f:
    games = [round[:-1].split(' ') for round in f]

# print(games)

for i, game_round in enumerate(games):
    opponent_play = game_round[0]
    strategy = game_round[1]

    # Play to lose
    if strategy == "X":
        if opponent_play == "A":
            games[i][1] = "C"
        elif opponent_play == "B":
            games[i][1] = "A"
        elif opponent_play == "C":
            games[i][1] = "B"

    # Play to draw
    elif strategy == "Y":
        games[i][1] = opponent_play

    # Play to win
    elif strategy == "Z":
        if opponent_play == "A":
            games[i][1] = "B"
        elif opponent_play == "B":
            games[i][1] = "C"
        elif opponent_play == "C":
            games[i][1] = "A"

print(games)

ROUND_SCORE = 0
TOTAL_SCORE = 0

for game_round in games:

    # Rock vs rock, tie
    if game_round == ["A", "A"]:
        ROUND_SCORE = 1 + 3

    # Rock vs paper, win
    elif game_round == ["A", "B"]:
        ROUND_SCORE = 2 + 6

    # Rock vs scissor, lose
    elif game_round == ["A", "C"]:
        ROUND_SCORE = 3 + 0

    # Paper vs rock, lose
    elif game_round == ["B", "A"]:
        ROUND_SCORE = 1 + 0

    # Paper vs paper, tie
    elif game_round == ["B", "B"]:
        ROUND_SCORE = 2 + 3

    # Paper vs scissor, win
    elif game_round == ["B", "C"]:
        ROUND_SCORE = 3 + 6

    # Scissor vs rock, win
    elif game_round == ["C", "A"]:
        ROUND_SCORE = 1 + 6

    # Scissor vs paper, lose
    elif game_round == ["C", "B"]:
        ROUND_SCORE = 2 + 0

    # Scissor vs scissor, tie
    elif game_round == ["C", "C"]:
        ROUND_SCORE = 3 + 3

    else:
        print(game_round)
        raise ValueError


    TOTAL_SCORE = TOTAL_SCORE + ROUND_SCORE

print(TOTAL_SCORE)
