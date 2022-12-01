
def solve(input: str):
    processed = sorted([sum([int(y) for y in x.split('\n')]) for x in input.split('\n\n')], reverse=True)

    print(processed[0] + processed[1] + processed[2])

def main():
    with open('./input.txt') as f:
        input = f.read()

    solve(input)

if __name__ == "__main__":
    main()