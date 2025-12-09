import os

base = os.path.dirname(__file__)
path = os.path.join(base, "input.txt")

answer = 0

def start():
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
        check_papers(lines)
    print(f"total answer: {answer}")

def check_papers(lines):
    new_lines = []
    total_lines: int = len(lines)

    for index, line in enumerate(lines):
        length = len(line)
        previous_line = lines[index - 1] if index - 1 >= 0 else None
        next_line = lines[index + 1] if index + 1 < total_lines else None
        new_lines.append(check_rows([previous_line, line, next_line], length))

    if new_lines == lines:
        return

    check_papers(new_lines)

def check_rows(lines: list[str | None], length: int):
    global answer
    current_line = lines[1]
    for index in range(length):
        if current_line[index] == ".":
            continue

        begin = max(0, index - 1)
        end = min(length - 1, index + 1)

        count = -1
        for line in lines:
            count += check_line(line, begin, end)
        if count < 4:
            current_line = current_line[:index] + "." + current_line[index + 1:]
            answer += 1
    return current_line

def check_line(line: str | None, begin: int, end: int) -> int:
    if line is None:
        return 0
    try:
        line = line[begin:end+1]
        return line.count("@")
    except IndexError:
        return 0

if __name__ == '__main__':
    start()