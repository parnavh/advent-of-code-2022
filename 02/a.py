
answers = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0,
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6,
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3,
    },
}

scores = [1, 2, 3]

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