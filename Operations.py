Stack = []

maze = [
    "#o######",
    "# ##   #",
    "# ## # #",
    "#    # #",
    "## ### #",
    "##  ## #",
    "######e#",
]



def start_index(maze):
    for index_line, line in enumerate(maze):

        for index_letter, letter in enumerate(line):
            if letter == "o":
                return index_line, index_letter

    return "This maze has no start"


def change(text, char, index):
    return text[:index] + char + text[(index+1):]


def is_up_cell_empty(line, letter):
    if line > 0:  # üstü tara

        if maze[line - 1][letter] == " ":
            maze[line-1] = change(maze[line - 1], "#", letter)
            return line - 1, letter

        elif maze[line - 1][letter] == "e":
            return f"End of this maze = {line - 1, letter}"


def is_down_cell_empty(line, letter):
    if line < len(maze):  # altı tara

        if maze[line + 1][letter] == " ":

            maze[line + 1] = change(maze[line + 1], "#", letter)
            return line + 1, letter

        elif maze[line + 1][letter] == "e":
            return f"End of this maze = {line + 1, letter}"


def is_left_cell_empty(line, letter):
    if letter > 0:  # solu tara

        if maze[line][letter - 1] == " ":
            maze[line] = change(maze[line], "#", letter - 1)
            return line, letter - 1

        elif maze[line + 1][letter] == "e":
            return f"End of this maze = {line, letter - 1}"


def is_right_cell_empty(line, letter):
    if letter < len(maze[0]):  # sağı tara

        if maze[line][letter + 1] == " ":
            maze[line] = change(maze[line], "#", letter + 1)
            return line, letter + 1

        elif maze[line + 1][letter + 1] == "e":
            return f"End of this maze = {line, letter + 1}"


def next(line, letter):
    if line == "first":
        line, letter = start_index(maze)
    print("siü")
    print(line, letter)
    print(maze)

    counter = 0
    if is_right_cell_empty(line, letter):
        counter += 1
        line, letter = is_right_cell_empty(line, letter)
        next(line, letter)

    if is_left_cell_empty(line, letter):
        counter += 1
        line, letter = is_left_cell_empty(line, letter)
        next(line, letter)

    if is_down_cell_empty(line, letter):
        counter += 1
        line, letter = is_down_cell_empty(line, letter)
        next(line, letter)

    if is_up_cell_empty(line, letter):
        counter += 1
        line, letter = is_up_cell_empty(line, letter)
        next(line, letter)

    if counter > 1:
        Stack.append((line, letter))


next("first", "first")

# print(start_index(maze))

