
def solve(input: list[str]):
    queue = []

    for i in range(len(input)):
        if len(queue) == 14:
            if len(set(queue)) == 14:
                print(i)
                break
            queue.pop(0)
            queue.append(input[i])
        else:
            queue.append(input[i])


def main():
    with open('./input.txt') as f:
        input = f.read()

    solve(input)

if __name__ == "__main__":
    main()