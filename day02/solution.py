import os

answer: int = 0

base = os.path.dirname(__file__)
path = os.path.join(base, "input.txt")

def start():
    global answer
    with open(path) as file:
        line = file.readline()
        x = line.split(",")
        for item in x:
            print(item)
            if item == "": continue
            try:
                values = item.split("-")
                begin: int = int(values[0])
                end: int = int(values[1])
                for i in range(begin, end+1):
                    odd_or_even(str(i))
                print(f"begin: {begin} ({len(str(begin))}), end: {end} ({len(str(end))})")
            except ValueError:
                print(f"ValueError: {item}")
        print(answer)

def odd_or_even(value: str):
    length: int = len(value)
    if length % 2 == 0:
        repeated(value, length)
    return

def repeated(value: str, length: int):
    global answer
    try:
        half: int = int(length/2)
        half_1: int = int(value[:half])
        half_2: int = int(value[half:])
        if half_1 == half_2:
            answer += int(value)
    except ValueError:
        print(f"ValueError: {value}")

start()