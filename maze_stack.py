from typing import List, Tuple

Stack = []

ROAD = " "
WALL = "#"
START = "o"
EXIT = "e"
STEP = "."


def start_index(labyrinth: List[str]) -> Tuple[int, int]:
    """
    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.

    :return: Returns the index of the START character in the list of strings
    """
    for index_line, line in enumerate(labyrinth):

        for index_letter, letter in enumerate(line):
            if letter == f"{START}":
                print(f"Start of this maze is {index_line}, {index_letter}")
                return index_line, index_letter

    raise Exception("This labyrinth has no start")


def change(text: str, char: str, index: int) -> str:
    """
    Replaces the letter in the specified index with the desired letter

    :param text: String
    :param char: New letter to replace the changed letter
    :param index: Index of the letter to be changed
    :return: Edited new string
    """
    return text[:index] + char + text[(index + 1):]


def is_up_cell_empty(labyrinth: List[str], line: int, letter: int) -> bool:
    """
    Returns whether a path exists in the full parent directory of the current location

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    :return: True or False
    """
    if line > 0:  # üstü tara
        if labyrinth[line - 1][letter] == ROAD:

            return True
        else:
            return False


def is_down_cell_empty(labyrinth: List[str], line: int, letter: int) -> bool:
    """
    Returns whether a path exists in the directory directly below the current location

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    :return: True or False
    """
    if line < len(labyrinth):  # altı tara
        if labyrinth[line + 1][letter] == ROAD:
            return True
        else:
            return False


def is_left_cell_empty(labyrinth: List[str], line: int, letter: int) -> bool:
    """
    Returns whether there is a path in the directory just to the left of the current location

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    :return: True or False
    """
    if letter > 0:  # solu tara
        if labyrinth[line][letter - 1] == ROAD:
            return True
        else:
            return False


def is_right_cell_empty(labyrinth: List[str], line: int, letter: int) -> bool:
    """
    Returns whether there is a path in the directory just to the right of the current location

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    :return: True or False
    """
    if letter < len(labyrinth[0]):  # sağı tara
        if labyrinth[line][letter + 1] == ROAD:
            return True
        else:
            return False


def stack_next_steps_and_edit(labyrinth: List[str], line: int, letter: int):
    """
        Closes(updates) the index just above the current location

        :param labyrinth: list of string structures with the same number of elements of the list and the same number of
        elements of arrays, having at least one continuous path from beginning to end.
        :param line: List(line) index of current location
        :param letter:String(letter) index of current location
        :return: Returns the index information of the character directly above the current position
        """
    if is_up_cell_empty(labyrinth, line, letter):
        labyrinth[line - 1] = change(labyrinth[line - 1], STEP, letter)
        Stack.append((line - 1, letter))

    if is_down_cell_empty(labyrinth, line, letter):
        labyrinth[line + 1] = change(labyrinth[line + 1], STEP, letter)
        Stack.append((line + 1, letter))

    if is_left_cell_empty(labyrinth, line, letter):
        labyrinth[line] = change(labyrinth[line], STEP, letter - 1)
        Stack.append((line, letter - 1))

    if is_right_cell_empty(labyrinth, line, letter):
        labyrinth[line] = change(labyrinth[line], STEP, letter + 1)
        Stack.append((line, letter + 1))


def exit_check(labyrinth: List[str], line: int, letter: int) -> bool:
    """
    It checks if there is an exit above the current location and if it finds exit, it prints the exit index
    information on the screen and shuts down the system.

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    """
    if line > 0:  # üstü tara
        if labyrinth[line - 1][letter] == EXIT:
            print(f"End of this maze is {line - 1},{letter}")
            return True

    if line < len(labyrinth):  # alti tara
        if labyrinth[line + 1][letter] == EXIT:
            print(f"End of this maze is {line + 1},{letter}")
            return True

    if letter > 0:  # solu tara
        if labyrinth[line][letter - 1] == EXIT:
            print(f"End of this maze is {line},{letter - 1}")
            return True

    if letter < len(labyrinth[0]):  # sagi tara
        if labyrinth[line][letter + 1] == EXIT:
            print(f"End of this maze is {line},{letter + 1}")
            return True


def runner(labyrinth: List[str], line=0, letter=0):
    while True:
        print(line, letter)
        for i in range(len(labyrinth)):
            print(labyrinth[i])

        if exit_check(labyrinth, line, letter):
            return
        stack_next_steps_and_edit(labyrinth, line, letter)

        line, letter = Stack.pop()


def start(labyrinth: List[str]):
    """
    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    """
    Stack.append(start_index(labyrinth))
    runner(labyrinth, *Stack.pop())
