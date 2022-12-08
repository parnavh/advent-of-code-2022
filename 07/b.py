import dpath

size = -1

def find_dir(files: dict, target: int):
    global size

    for key, value in files.items():
        if key == '_size' and value >= target:
            if value < size or size == -1:
                size = value

        if type(value) == dict:
            find_dir(value, target)

def solve(input: list[str]):
    files = {
        '/': {
            '_size': 0
        }
    }
    path = []
    for line in input:
        chars = line.split(' ')

        if chars[0] == '$':
            if chars[1] == 'cd':
                if chars[2] == '..':
                    path.pop()
                else:
                    path.append(chars[2])

            continue

        try:
            dpath.get(files, path + [chars[1]])
        except KeyError:
            if chars[0] == 'dir':
                dpath.new(files, path + [chars[1]], { '_size' : 0 })
            else:
                dpath.new(files, path + [chars[1]], int(chars[0]))
                for sub in range(1, len(path) + 1):
                    dpath.set(files, path[:sub] + ['_size'], dpath.get(files, path[:sub] + ['_size']) + int(chars[0]))

    find_dir(files, 30000000 + files['/']['_size'] - 70000000)

    print(size)


def main():
    with open('./input.txt') as f:
        input = f.read()

    solve(input.splitlines())

if __name__ == "__main__":
    main()