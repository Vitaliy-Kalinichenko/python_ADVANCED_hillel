# 1) Write a function that emulates the game "rock, scissors, paper"
# At the entrance, your function accepts your version printed from the console, the computer makes a decision randomly.
# На входе ваша функция принимает вашу версию, напечатанную с консоли, компьютер принимает решение случайным образом.
from random import randint


def game(sign):
    signs = ('rock', 'scissors', 'paper')
    if sign in signs:
        sign_computer = signs[randint(0, 2)]
        print(sign_computer)
        list_win = (('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock'))
        if sign == sign_computer:
            return 'draw'
        elif (sign, sign_computer) in list_win:
            return 'You win'
        return 'You lose'
    return 'incorrect input, please try again'


print(game(input('Enter rock, scissors or paper> ').lower()))

# 2)Try to imagine a world in which you might have to stay home for (Corona virus) 14 days at any given time.
# Do you have enough toilet paper(TP) to make it through?
# Although the number of squares per roll of TP varies significantly, we'll assume each roll has 500 sheets,
# and the average person uses 57 sheets per day.
import math

days = 14
sheets_in_roll = 500
average_sheets = 57


def count_tp(d):
    if isinstance(d, dict) and d.get("people") and d.get('tp'):
        required_tp = math.ceil(days * d.get('people') * average_sheets / sheets_in_roll)
        if d.get("tp") < required_tp:
            return f'You need to buy {required_tp - d.get("tp")} TP'
        return 'You have enough TP'
    return 'wrong data'


d = {
    'people': 4,
    'tp': 5
}
print(count_tp(d))


# Попробуйте представить себе мир, в котором вам, возможно, придется оставаться дома (вирус короны) 14 дней в любой момент времени.
# Достаточно ли у вас туалетной бумаги (TP), чтобы пережить это?
# Хотя количество квадратов в рулоне TP значительно различается, мы предполагаем, что каждый рулон содержит 500 листов,
# и в среднем человек использует 57 листов в день.
# # Создайте функцию, которая будет получать словарь с двумя парами "ключ-значение": "люди"  - количество человек в семье.
# «tp» - Количество рулонов. Верните сообщение пользователю, если ему нужно купить больше TP!

# Create a function that will receive a dictionary with two key/values:
# "people" ⁠— Number of people in the household.
# "tp" ⁠— Number of rolls.
# Return a statement telling the user if they need to buy more TP!

# 3) Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# Создайте функцию, которая шифрует данный ввод, выполнив следующие действия:
# Ввод: «яблоко»
# Шаг 1. Поменяйте местами ввод: "elppa"
# Шаг 2: замените все гласные, используя следующую таблицу
# a = > 0
# e = > 1
# i = > 2
# o = > 2
# u = > 3


# # "1lpp0"
# Example:
# encrypt("banana") ➞ "0n0n0b"
# encrypt("karaca") ➞ "0c0r0k"
# encrypt("burak") ➞ "k0r3b"
# encrypt("alpaca") ➞ "0c0pl0"
def encrypts(value):
    d = {
        'a': 0,
        'e': 1,
        'i': 2,
        'o': 2,
        'u': 3
    }
    return ''.join([str(d[i]) if i in d else i for i in value[::-1]])


print(encrypts(input().lower()))


# **4)Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win
# for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.
# Учитывая матрицу 3x3 завершенной игры в крестики-нолики, создайте функцию, которая возвращает, является ли игра выигрышной
# для «X», «O» или «Ничья», где «X» и «O» представляют сами себя. на матрице, а «E» представляет собой пустое место.
# Example:
# tic_tac_toe([
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["O", "X", "X"]
# ]) ➞ "X"
#
# tic_tac_toe([
#     ["O", "O", "O"],
#     ["O", "X", "X"],
#     ["E", "X", "X"]
# ]) ➞ "O"
#
# tic_tac_toe([
#     ["X", "X", "O"],
#     ["O", "O", "X"],
#     ["X", "X", "O"]
# ]) ➞ "Draw"
def tic_tac_toe(matrix):
    win_x = ["X", "X", "X"]
    win_0 = ["O", "O", "O"]
    columns = list(zip(*matrix))
    main_diagonal = [matrix[i][j] for i in range(3) for j in range(3) if i == j]
    second_diagonal = [matrix[i][-i - 1] for i in range(3)]
    if tuple(win_0) in columns or win_0 in matrix or win_0 == main_diagonal or win_0 == second_diagonal:
        return "O"
    elif tuple(win_x) in columns or win_x in matrix or win_x == main_diagonal or win_x == second_diagonal:
        return "X"
    return "Draw"


print(tic_tac_toe([
    ["O", "O", "E"],
    ["O", "X", "X"],
    ["O", "X", "X"]
]))
print(tic_tac_toe([
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]))

print(tic_tac_toe([
    ["O", "O", "O"],
    ["O", "X", "X"],
    ["E", "X", "X"]
]))

print(tic_tac_toe([
    ["X", "X", "O"],
    ["O", "O", "X"],
    ["X", "X", "O"]
]))

print(tic_tac_toe([
    ["X", "X", "O"],
    ["O", "O", "X"],
    ["O", "X", "O"]
]))
