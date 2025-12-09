import os

base = os.path.dirname(__file__)
path = os.path.join(base, 'test_input.txt')

answer = 0

def start():
    with open(path) as file:
        lines = [line.strip() for line in file.readlines()]
        ranges: list[tuple[int, int]] = []
        items: list[int] = []
        for line in lines:
            if line == "":
                continue
            if "-" in line:
                ranges.append(get_range(line))
            else:
                items.append(get_item(line))

        print(f"ranges: {ranges}, items: {items}")
        get_total_amount(items, ranges, 0)


def get_range(line: str) -> tuple[int, int]:
    string: list[str] = line.split("-")
    return int(string[0]), int(string[1])

def get_item(line: str) -> int:
    return int(line)

def get_fresh_food(items: list[int], range: tuple[int, int]):
    global answer
    checked_items: list[int] = []
    for item in items:
        if item is None:
            continue

        print(f"item: {item}")
        if item < range[0]:
            print("a")
            checked_items.append(item)
        elif item > range[1]:
            print("b")
            break
        else:
            print("c")
            answer += 1
            checked_items.append(item)
    remaining_items: list[int] = items
    for item in checked_items:
        remaining_items.remove(item)
    print(f"new_items: {checked_items}")
    print(f"newest_items: {remaining_items}")
    return remaining_items

def get_total_amount(items: list[int], ranges: list[tuple[int, int]], range_index: int):
    global answer
    if items[0] is None or range_index >= len(ranges):
        print(f"total answer: {answer}")
    else:
        items = get_fresh_food(items, ranges[range_index])
        get_total_amount(items, ranges, range_index + 1)



if __name__ == '__main__':
    start()