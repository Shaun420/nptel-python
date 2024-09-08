"""
Question
You are given a board game scenario with ladders and snakes. A player starts at a given position on the board, and you are provided with the result of a die roll. You need to determine whether the player lands on a ladder, a snake, or a normal block after moving.

Write a Python function named move_player that takes four inputs:

    A list ladders containing the indices of blocks with ladders.
    A list snakes containing the indices of blocks with snakes.
    An integer current_position representing the player's current position on the board.
    An integer die_roll representing the result of a die roll.

The function should return:

    1 if the player lands on a block with a ladder,
    -1 if the player lands on a block with a snake,
    0 if the player lands on a block with neither.

Take necessary inputs, pass the inputs to the function, and print the return value of the function.

Input Format
The input consists of four lines:

    The first line contains space-separated integers representing the ladder indices.
    The second line contains space-separated integers representing the snake indices.
    The third line contains a single integer representing the current position of the player.
    The fourth line contains a single integer representing the die roll result.

Output Format
The output consists of a single integer (1, -1, or 0) as per the conditions mentioned above.
"""

inputlist = input().split(" ")
ladders = list(map(int, inputlist))
inputlist = input().split(" ")
snakes = list(map(int, inputlist))
current_position = int(input())
die_roll = int(input())
def move_player(ladders, snakes, current_position, die_roll):
  current_position += die_roll
  if current_position in ladders:
    return 1
  elif current_position in snakes:
    return -1
  else:
    return 0

print(move_player(ladders, snakes, current_position, die_roll), end="")
