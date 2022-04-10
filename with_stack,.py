from typing import List, Tuple

Stack = []

MAZE = [
    "#o######",
    "# ##   #",
    "# ## # #",
    "#    # #",
    "## ### #",
    "##  ## #",
    "######e#",
]


def start_index(labyrint: List[str]) -> Tuple[int, int]:
    for index_line, line in enumerate(labyrint):

        for index_letter, letter in enumerate(line):
            if letter == "o":
                return index_line, index_letter

    raise Exception("This labyrint has no start")


def change(text, char, index):
    return text[:index] + char + text[(index + 1):]


def is_up_cell_empty(labyrint, line, letter):
    if line > 0:  # üstü tara
        if labyrint[line - 1][letter] == "e":
            raise Exception(f"End of this maze is {line - 1},{letter}")
        if labyrint[line - 1][letter] == " ":

            return True
        else:
            return False


def edit_up(labyrint, line, letter):
    labyrint[line - 1] = change(labyrint[line - 1], "#", letter)
    return line - 1, letter


def is_down_cell_empty(labyrint, line, letter):
    if line < len(labyrint):  # altı tara
        if labyrint[line + 1][letter] == "e":
            print(f"End of this maze is {line + 1},{letter}")
        if labyrint[line + 1][letter] == " ":
            return True
        else:
            return False


def edit_down(labyrint, line, letter):
    labyrint[line + 1] = change(labyrint[line + 1], "#", letter)
    return line + 1, letter


def is_left_cell_empty(labyrint, line, letter):
    if letter > 0:  # solu tara
        if labyrint[line][letter - 1] == "e":
            return Exception (f"End of this maze is {line},{letter - 1}")
        if labyrint[line][letter - 1] == " ":
            return True
        else:
            return False


def edit_left(labyrint, line, letter):
    labyrint[line] = change(labyrint[line], "#", letter - 1)
    return line, letter - 1


def is_right_cell_empty(labyrint, line, letter):
    if letter < len(labyrint[0]):  # sağı tara

        if labyrint[line][letter + 1] == "e":
            raise Exception (f"End of this maze is {line},{letter + 1}")
        if labyrint[line][letter + 1] == " ":
            return True
        else:
            return False


def edit_right(labyrint, line, letter):
    labyrint[line] = change(labyrint[line], "#", letter + 1)
    return line, letter + 1


def next(labyrint, line, letter):
    if line == "first":
        line, letter = start_index(labyrint)

    print(line, letter)

    counter = 0
    if is_right_cell_empty(labyrint, line, letter):
        line, letter = edit_right(labyrint, line, letter)
        counter += 1
        next(MAZE, line, letter)

    if is_left_cell_empty(labyrint, line, letter):
        line, letter = edit_left(labyrint, line, letter)
        counter += 1
        next(MAZE, line, letter)

    if is_down_cell_empty(labyrint, line, letter):
        line, letter = edit_down(labyrint, line, letter)
        counter += 1
        next(MAZE, line, letter)

    if is_up_cell_empty(labyrint, line, letter):
        line, letter = edit_up(labyrint, line, letter)
        counter += 1
        next(MAZE, line, letter)

    if counter > 1:
        Stack.append((line, letter))

next(MAZE, "first", "first")

# print(start_index(labyrint))
