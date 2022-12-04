
def solve(input: list[str]):
    count = 0
    for line in input:
        a, b = [[int(a) for a in x.split('-')] for x in line.split(',')]
        if a[0] == b[0] or a[1] == b[1]:
            count += 1
        elif a[0] < b[0] and a[1] > b[1]:
            count += 1
        elif b[0] < a[0] and b[1] > a[1]:
            count += 1
        elif a[0] < b[0] and a[1] < b[1] and a[1] >= b[0]:
            count += 1
        elif b[0] < a[0] and b[1] < a[1] and b[1] >= a[0]:
            count += 1
    print(count)

def main():
    with open('./input.txt') as f:
        input = f.read()

    solve(input.splitlines())

if __name__ == "__main__":
    main()