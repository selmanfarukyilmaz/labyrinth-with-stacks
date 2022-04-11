import sys

from typing import List, Tuple

Stack = []

ROAD = " "
WALL = "#"
START = "o"
EXIT = "e"


def start_index(labyrinth: List[str]) -> Tuple[int, int]:
    """
    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.

    :return: Returns the index of the START character in the list of strings
    """
    for index_line, line in enumerate(labyrinth):

        for index_letter, letter in enumerate(line):
            if letter == f"{START}":
                print(f"End of this maze is {index_line}, {index_letter}")
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
        if labyrinth[line - 1][letter] == f"{ROAD}":

            return True
        else:
            return False


def edit_up(labyrinth: List[str], line: int, letter: int) -> tuple:
    """
    Closes(updates) the index just above the current location

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    :return: Returns the index information of the character directly above the current position
    """
    labyrinth[line - 1] = change(labyrinth[line - 1], f"{WALL}", letter)
    return line - 1, letter


def is_up_cell_exit(labyrinth: List[str], line: int, letter: int):
    """
    It checks if there is an exit above the current location and if it finds exit, it prints the exit index
    information on the screen and shuts down the system.

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    """
    if line > 0:  # üstü tara
        if labyrinth[line - 1][letter] == f"{EXIT}":
            print(f"End of this maze is {line - 1},{letter}")
            sys.exit()


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
        if labyrinth[line + 1][letter] == f"{ROAD}":
            return True
        else:
            return False


def edit_down(labyrinth: List[str], line: int, letter: int) -> tuple:
    """
    Closes (updates) the directory just below the current location

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    :return: Returns the index information of the character directly below the current position
    """
    labyrinth[line + 1] = change(labyrinth[line + 1], f"{WALL}", letter)
    return line + 1, letter


def is_down_cell_exit(labyrinth: List[str], line: int, letter: int):
    """
    It checks if there is an exit under the current location and if it finds exit, it prints the exit index
    information on the screen and shuts down the system.

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    """
    if line < len(labyrinth):  # altı tara
        if labyrinth[line + 1][letter] == f"{EXIT}":
            print(f"End of this maze is {line + 1},{letter}")
            sys.exit()


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
        if labyrinth[line][letter - 1] == f"{ROAD}":
            return True
        else:
            return False


def edit_left(labyrinth: List[str], line: int, letter: int) -> tuple:
    """
    Closes (updates) the directory just to the left of the current location

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    :return: Returns the index information of the character directly left of the current position
    """
    labyrinth[line] = change(labyrinth[line], f"{WALL}", letter - 1)
    return line, letter - 1


def is_left_cell_exit(labyrinth: List[str], line: int, letter: int):
    """
    It checks whether there is an exit to the left of the current location and if it finds exit, it prints the exit
    index information on the screen and shuts down the system.

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    """
    if letter > 0:  # solu tara
        if labyrinth[line][letter - 1] == f"{EXIT}":
            print(f"End of this maze is {line},{letter - 1}")
            return True


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
        if labyrinth[line][letter + 1] == f"{ROAD}":
            return True
        else:
            return False


def edit_right(labyrinth: List[str], line: int, letter: int) -> tuple:
    """
    Closes (updates) the directory just to the right of the current location

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    :return: Returns the index information of the character directly right of the current position
    """
    labyrinth[line] = change(labyrinth[line], f"{WALL}", letter + 1)
    return line, letter + 1


def is_right_cell_exit(labyrinth: List[str], line: int, letter: int):
    """
    It checks whether there is an exit to the right of the current location and if it finds exit, it prints the exit
    index information on the screen and shuts down the system.


    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    """
    if letter < len(labyrinth[0]):
        if labyrinth[line][letter + 1] == f"{EXIT}":
            print(f"End of this maze is {line},{letter + 1}")
            sys.exit()


def exit_check(labyrinth: List[str], line: int, letter: int):
    """
    If it checks the exit character on all 4 sides of the current index and finds the exit, the system shuts down.

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    """
    is_up_cell_exit(labyrinth, line, letter)
    is_down_cell_exit(labyrinth, line, letter)
    is_left_cell_exit(labyrinth, line, letter)
    is_right_cell_exit(labyrinth, line, letter)


def runner(labyrinth: List[str], line=0, letter=0):
    """
    It checks if there is ROAD on all 4 sides of the current index, when it finds ROAD, it assigns the index
    information of this ROAD to the Stack as a tuple and updates this ROAD as WALL. Using the tuples holding the
    index information thrown to the stack, the same function is recursively performed and the result is the exit of
    the maze.

    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    :param line: List(line) index of current location
    :param letter:String(letter) index of current location
    """
    counter = 0
    if is_right_cell_empty(labyrinth, line, letter):
        new_line, new_letter = edit_right(labyrinth, line, letter)
        Stack.append((new_line, new_letter))
        counter += 1

    if is_left_cell_empty(labyrinth, line, letter):
        new_line, new_letter = edit_left(labyrinth, line, letter)
        Stack.append((new_line, new_letter))
        counter += 1

    if is_down_cell_empty(labyrinth, line, letter):
        new_line, new_letter = edit_down(labyrinth, line, letter)
        Stack.append((new_line, new_letter))
        counter += 1

    if is_up_cell_empty(labyrinth, line, letter):
        new_line, new_letter = edit_up(labyrinth, line, letter)
        Stack.append((new_line, new_letter))
        counter += 1

    if counter <= 1:
        if Stack:
            exit_check(labyrinth, line, letter)
            line, letter = Stack.pop()
            print(line, letter)
            runner(labyrinth, line, letter)

    if counter > 1:
        for i in range(counter):
            if Stack:
                exit_check(labyrinth, line, letter)
                line, letter = Stack.pop()
                print(line, letter)
                runner(labyrinth, line, letter)
                if exit_check(labyrinth, line, letter):
                    return


def start(labyrinth: List[str]):
    """
    :param labyrinth: list of string structures with the same number of elements of the list and the same number of
    elements of arrays, having at least one continuous path from beginning to end.
    """
    line, letter = start_index(labyrinth)
    runner(labyrinth, line, letter)
