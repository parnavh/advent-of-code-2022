
def solve(input: str):
    lowercase = [x for x in range(1, 27)]
    uppercase = [x for x in range(27, 53)]

    total = 0
    v = {}
    i = 0

    for line in input.splitlines():
        for ch in set(line):
            v[ch] = v.get(ch, 0) + 1
        i += 1

        if i == 3:
            for ch in v:
                if v[ch] == 3:
                    if ch.islower():
                        total += lowercase[ord(ch) - ord('a')]
                    else:
                        total += uppercase[ord(ch) - ord('A')]
                    break
            v = {}
            i = 0

    print(total)

def main():
    with open('./input.txt') as f:
        input = f.read()

    solve(input)

if __name__ == "__main__":
    main()