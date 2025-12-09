def part_2(self, filepath: str):
    result, pos, mod = 0, 50, 100

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            d, n = line[0], int(line[1:])
            full, rest = divmod(n, mod)
            result += full

            if d == "L":
                if pos != 0 and pos - rest <= 0:
                    result += 1
                pos = (pos - n) % mod
            else:
                if pos + rest >= mod:
                    result += 1
                pos = (pos + n) % mod

    return result

print(part_2(None, 'input.txt'))