import os

base = os.path.dirname(__file__)
path = os.path.join(base, "input.txt")
total_answer: list[int] = []

def start():
    global total_answer
    with open(path) as file:
        for line in file.readlines():
            int_list: list[int] = []
            line = line.strip()
            for s in line:
                int_list.append(int(s))

            answer: list[int] = []
            battery_amount: int = 12

            for i in range(battery_amount):
                highest_number: tuple[int, int] = get_highest_number(int_list, battery_amount - i)
                answer.append(highest_number[0])
                int_list = short_list(int_list, highest_number[1])
            total_answer.append(make_number(answer))
    calculate_total()

def get_highest_number(int_list: list[int], index: int) -> tuple[int, int]:
    highest_number: int = max(int_list)
    highest_number = (check_number(int_list, highest_number, index))
    return highest_number, int_list.index(highest_number)

def check_number(int_list: list[int], highest_number: int, index: int, fails: int = 0) -> int:
    if len(int_list) - int_list.index(highest_number) >= index:
        return highest_number
    else:
        fails += 1
        sorted_list: list[int] = sorted(int_list, reverse=True)
        highest_number = sorted_list[fails]
        return check_number(int_list, highest_number, index, fails)


def short_list(int_list: list[int], index: int) -> list[int]:
    return int_list[index + 1:]

def calculate_total():
    global total_answer
    print(sum(total_answer))

def make_number(int_list: list[int]) -> int:
    string: str = ""
    for number in int_list:
        string += str(number)
    return int(string)

if __name__ == "__main__":
    start()