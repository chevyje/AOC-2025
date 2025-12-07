import os

base = os.path.dirname(__file__)
path = os.path.join(base, "input.txt")
answer: list[int] = []

def start():
    global answer
    with open(path) as file:
        for line in file.readlines():
            int_list: list[int] = []
            line = line.strip()
            for s in line:
                int_list.append(int(s))
            highest_number: tuple[int, int] = get_highest_number(int_list)
            shorter_list = short_list(int_list, highest_number[1])
            second_number: int = max(shorter_list)
            total = int(str(highest_number[0]) + str(second_number))
            answer.append(total)
    calculate_total()

def get_highest_number(int_list: list[int]) -> tuple[int, int]:
    sorted_list: list[int] = sorted(int_list, reverse=True)
    highest_number: int = sorted_list[0]
    index_highest: int = int_list.index(highest_number)
    length = len(int_list)
    if index_highest >= length - 1:
        highest_number = sorted_list[1]
        index_highest = int_list.index(highest_number)
    return highest_number, index_highest

def short_list(int_list: list[int], index: int) -> list[int]:
    return int_list[index + 1:]

def calculate_total():
    global answer
    total: int = 0
    for i in answer:
        total += i
    print (total)

if __name__ == "__main__":
    start()