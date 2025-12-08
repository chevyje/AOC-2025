import os

base = os.path.dirname(__file__)
path = os.path.join(base, "test_input.txt")

answer = 0

def start():
    with open(path) as file:
        lines = file.readlines()
        total_lines: int = len(lines)
        for index, line in enumerate(lines):
            length = len(line.strip())
            previous_line = None
            next_line = None
            if index - 1 >= 0:
                previous_line = lines[index-1].strip()
            if index + 1 <= total_lines - 1:
                next_line = lines[index+1].strip()

            check_rows([previous_line, line.strip(), next_line], length)
            print(f"line {index}: {line} \n")
    print(f"total answer: {answer}")

def check_rows(lines: list[str | None], length: int):
    global answer
    for index in range(length):
        current_line = lines[1].strip()
        print(f"{index}: {current_line[index]}")
        if current_line[index] == ".":
            continue

        begin = 0
        end = length
        if index - 1 > 0:
            begin = index -1
        if index + 1 < length:
            end = index + 1

        count = -1
        for line in lines:
            count += check_line(line, begin, end)
        print(f"amount of @ around: {count}")
        if count < 4:
            answer += 1
            print(f"current answer: {answer} \n")

def check_line(line: str | None, begin: int, end: int) -> int:
    if line is None:
        return 0
    try:
        line = line.strip()
        line = line[begin:end+1]
        print(line)
        return line.count("@")
    except IndexError:
        return 0

if __name__ == '__main__':
    start()