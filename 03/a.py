
def solve(input: str):
    lowercase = [x for x in range(1, 27)]
    uppercase = [x for x in range(27, 53)]

    total = 0

    for line in input.splitlines():
        mid = len(line) // 2
        a, b = line[:mid], line[mid:]
        v = {}
        for ch in a:
            v[ch] = v.get(ch, 0) + 1

        for ch in b:
            if ch in v and v[ch] != 0:
                v[ch] = 0
                if ch.islower():
                    total += lowercase[ord(ch) - ord('a')]
                else:
                    total += uppercase[ord(ch) - ord('A')]

    print(total)

def main():
    with open('./input.txt') as f:
        input = f.read()

    solve(input)

if __name__ == "__main__":
    main()