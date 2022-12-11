
max = 0

def count(arr: list[str], i: int, j: int, x: int, y: int):
    global max
    count = 1

    k = j + 1
    hmm = 1
    while k < x - 1 and int(arr[i][k]) < int(arr[i][j]):
        hmm += 1
        k += 1

    count *= hmm

    k = j - 1
    hmm = 1
    while k > 0 and int(arr[i][k]) < int(arr[i][j]):
        hmm += 1
        k -= 1

    count *= hmm

    k = i + 1
    hmm = 1
    while k < y - 1 and int(arr[k][j]) < int(arr[i][j]):
        hmm += 1
        k += 1

    count *= hmm

    k = i - 1
    hmm = 1
    while k > 0 and int(arr[k][j]) < int(arr[i][j]):
        hmm += 1
        k -= 1

    count *= hmm

    max = count if count > max else max

def solve(input: list[str]):
    y = len(input)
    x = len(input[0])

    for i in range(y):
        for j in range(x):
            count(input, i, j, x, y)

    print(max)


def main():
    with open('./input.txt') as f:
        input = f.read()

    solve(input.splitlines())

if __name__ == "__main__":
    main()