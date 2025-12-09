def part_1(self, filepath: str):
    result = 0
    position = 50            # position initiale
    modulus = 100            # valeur maximale avant retour à 0

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # ignorer les lignes vides
            if not line:
                continue

            # Vérification de validité : première lettre = L ou R
            direction = line[0]
            if direction not in ("L", "R"):
                raise ValueError(f"Ligne invalide : {line}")

            # Extraction du nombre
            try:
                value = int(line[1:])
            except ValueError:
                raise ValueError(f"Nombre invalide dans la ligne : {line}")

            # Mise à jour de la position
            if direction == "L":
                position -= value
            else:
                position += value

            # gestion modulo
            position %= modulus

            # Test final
            if position == 0:
                result += 1

    return result


print(part_1(None, 'input.txt'))  # appel de la fonction avec le fichier d'entrée