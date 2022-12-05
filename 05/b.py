from re import split, findall

def solve(input: list[str]):
    switch = False
    silos = [[] for _ in range(9)]
    for line in input:
        if line == '':
            switch = True
            for i, silo in enumerate(silos):
                silos[i] = silo[::-1]
            continue

        if not switch:
            data = [a[1] if len(a) > 1 else a for a in split(r'\s+', line.strip())]
            for i, x in enumerate(data):
                if x == '1': break
                if x == '0': continue
                silos[i].append(x)
        else:
            number, from_silo, to_silo = [int(a) for a in findall(r'\d+', line)]
            n = len(silos[from_silo - 1]) - number
            silos[to_silo - 1].extend(silos[from_silo - 1][n:])
            del silos[from_silo - 1][n:]

    print(''.join([x[len(x) - 1] for x in silos]))

def main():
    with open('./input.txt') as f:
        input = f.read()

    solve(input.splitlines())

if __name__ == "__main__":
    main()