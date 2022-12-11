
def visible(line: str, j: int):
    lower = line[:j]
    upper = line[j + 1:]
    number = int(line[j])
    nums = [str(i) for i in range(number, 10)]
    return not (any([num in lower for num in nums]) and any([num in upper for num in nums]))

def solve(input: list[str]):
    visited = set()
    count = 0

    n = len(input)
    m = len(input[0])

    for i, line in enumerate(input):
        visited.add((i, 0))
        visited.add((i, m - 1))
        count += 2
        for j in range(1, m - 1):
            if visible(line, j) and (i, j) not in visited:
                visited.add((i, j))
                count += 1

    for i in range(m):
        line = ''.join([input[j][i] for j in range(n)])
        if (0, i) not in visited:
            visited.add((0, i))
            count += 1

        if ((n - 1, i) not in visited):
            visited.add((n - 1, i))
            count += 1
        for j in range(1, n - 1):
            if visible(line, j) and (j, i) not in visited:
                visited.add((j, i))
                count += 1

    print(count)


def main():
    with open('./input.txt') as f:
        input = f.read()

    solve(input.splitlines())

if __name__ == "__main__":
    main()