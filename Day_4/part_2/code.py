import numpy as np


def read_input(path):
    with open(path, "r") as f:
        return f.read().strip()


def parse_input(input_text):
    return np.array([list(row) for row in input_text.split("\n")])


def count_roles(mat, clear=False):
    rows, cols = mat.shape
    result = 0

    # Offsets des 8 voisins
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
         (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # On copie pour pouvoir modifier après le scan
    if clear:
        new_mat = mat.copy()

    for i in range(rows):
        for j in range(cols):

            # JS : on ne traite que les '@'
            if mat[i, j] != '@':
                continue

            count = 0

            # Compter les 8 voisins
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if mat[ni, nj] == '@':
                        count += 1

            # JS : condition => moins de 4 voisins @
            if count < 4:
                result += 1
                if clear:
                    new_mat[i, j] = '.'  # JS: mat[i][j] = "."

    if clear:
        mat[:, :] = new_mat

    return result


def part1(input_path):
    mat = parse_input(read_input(input_path))
    return count_roles(mat, clear=False)


def part2(input_path):
    mat = parse_input(read_input(input_path))

    total = 0
    result = None

    while result != 0:
        result = count_roles(mat, clear=True)
        total += result

    return total


print("Part 2:", part2("input.txt"))