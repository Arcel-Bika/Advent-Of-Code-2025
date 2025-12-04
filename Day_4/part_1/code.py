import numpy as np

data = np.loadtxt('input.txt', dtype=str)
mat = np.array([list(row) for row in data])

rows, cols = mat.shape

temp = 0

# 8 directions (haut, bas, gauche, droite + diagonales)
directions = [
    (-1,  0), (1,  0),    # haut, bas
    (0, -1), (0,  1),    # gauche, droite
    (-1, -1), (-1, 1),   # diagonales haut-gauche, haut-droite
    (1, -1),  (1,  1)    # diagonales bas-gauche, bas-droite
]

for i in range(rows):
    for j in range(cols):

        # Ne traiter que les '@'
        if mat[i, j] != '@':
            continue

        voisins = []

        # Collecter les 8 voisins
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                voisins.append(mat[ni, nj])

        # Nombre de voisins '@'
        nb_arobas = voisins.count('@')

        # Incrément si moins de 4 @ parmi les voisins
        if nb_arobas < 4:
            temp += 1

print("temp =", temp)
