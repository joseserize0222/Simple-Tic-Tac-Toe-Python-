def print_matrix(s):
    print("-" * 9)
    for i, c in enumerate(s):
        if i % 3 == 0:
            print("|", end=" ")
        print(c, end=" ") if c != "_" else print(" ", end = " ")
        if (i + 1) % 3 == 0:
            print("|")
    print("-" * 9)


def state(matrix):
    x_wins = False
    o_wins = False

    for i in range(3):
        if matrix[i].count("X") == 3:
            x_wins = True
        if matrix[i].count("O") == 3:
            o_wins = True

    #  print(x_wins, o_wins)

    for i in range(3):
        x_count = 0
        o_count = 0
        for j in range(3):
            if matrix[j][i] == "X":
                x_count += 1
            elif matrix[j][i] == "O":
                o_count += 1
        if x_count == 3:
            x_wins = True
        if o_count == 3:
            o_wins = True

    #  print(x_wins, o_wins)

    x_count = 0
    o_count = 0

    for i in range(3):
        if matrix[i][i] == "X":
            x_count += 1
        if matrix[i][i] == "O":
            o_count += 1

    if x_count == 3:
        x_wins = True
    if o_count == 3:
        o_wins = True

    #  print(x_wins, o_wins)

    l = 2
    x_count = 0
    o_count = 0

    for i in range(3):
        if matrix[i][l] == "X":
            x_count += 1
        if matrix[i][l] == "O":
            o_count += 1
        l -= 1

    if x_count == 3:
        x_wins = True
    if o_count == 3:
        o_wins = True

    #  print(x_wins, o_wins)

    impossible = True
    if abs(s.count("X") - s.count("O")) > 1:
        impossible = False
    impossible &= not (x_wins & o_wins)

    game_not_finished = s.__contains__("_")

    if not impossible:
        print("Impossible")
    elif x_wins:
        print("X wins")
        return True
    elif o_wins:
        print("O wins")
        return True
    elif not game_not_finished:
        print("Draw")
        return True
    else:
        return False


def modify(s: str, turn):
    char = ["O", "X"]
    while True:

        try:
            x, y = input().split()
            x = int(x)
            y = int(y)

            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Coordinates should be from 1 to 3!")
                continue
            elif s[(x-1)*3 + y-1] != "_":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                s = s[:(x-1)*3 + y-1] + char[turn] + s[(x-1)*3 + y:]
                break
        except ValueError:
            print("You should enter numbers!")
            continue

    return s

def to_matrix(s: str):
    return [[s[j] for j in range(3 * i, 3 * i + 3)] for i in range(3)]


s = "_________"

print_matrix(s)
matrix = to_matrix(s)
turn = 0

while not state(matrix):
    s = modify(s,1-turn)
    print_matrix(s)
    matrix = to_matrix(s)
    turn = 1-turn


