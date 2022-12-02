
answers = {
    'A': {
        'X': 3,
        'Y': 1,
        'Z': 2,
    },
    'B': {
        'X': 1,
        'Y': 2,
        'Z': 3,
    },
    'C': {
        'X': 2,
        'Y': 3,
        'Z': 1,
    },
}

scores = [0, 3, 6]

def solve(input: str):
    score = 0
    lines = input.split('\n')
    for line in lines:
        a, b = line.split(' ')
        score += scores[ord(b) - ord('X')] + answers[a][b]

    print(score)

def main():
    with open('./input.txt') as f:
        input = f.read()

    solve(input)

if __name__ == "__main__":
    main()