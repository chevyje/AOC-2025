import os

answer: set[int] = set()

base = os.path.dirname(__file__)
path = os.path.join(base, "input.txt")

def start():
    global answer
    with open(path) as file:
        line = file.readline()
        x: list[str] = line.split(",")
        for item in x:
            if item == "": continue
            try:
                values = item.split("-")
                begin: int = int(values[0])
                end: int = int(values[1])
                for i in range(begin, end+1):
                    odd_or_even(str(i))
            except ValueError:
                print(f"ValueError: {item}")
        total_answer()

def odd_or_even(value: str):
    length: int = len(value)
    for x in range(1, 10):
        if length % x == 0:
            repeated(value, length, x)
    return

def repeated(value: str, length: int, divided: int):
    global answer
    try:
        parts: set[int] = set()
        for i in range(0, length, divided):
            parts.add(int(value[i:i + divided]))

        if len(parts) == 1 and int(value) not in parts:
            print(f"added answer: {value}")
            answer.add(int(value))
    except ValueError:
        print(f"ValueError: {value}")

def total_answer():
    global answer
    total: int = 0
    for item in answer:
        total += item

    print(total)

start()