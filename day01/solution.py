import os

start_dial: int = 50
zero_count: int = 0
previous_dial: int = start_dial
current_dial: int = start_dial

base = os.path.dirname(__file__)
path = os.path.join(base, 'input.txt')

def start():
    global zero_count
    with open(path) as file:
        for line in file:
            try:
                line = line.strip()
                amount_value: int = int(line[1:])
                rotation_value: str = line[:1]
                turn(amount_value, rotation_value)
            except ValueError:
                print("Something went wrong")
                quit()

    print(zero_count)

def turn(amount: int, rotation: str) -> None:
    global current_dial
    global zero_count
    global previous_dial
    amount = check_rounds(amount)

    if rotation == 'R':
        current_dial += amount
    elif rotation == 'L':
        current_dial -= amount
    else:
        print ("Something went wrong")
        quit()

    back_to_dial()
    if current_dial == 0:
        zero_count += 1
    previous_dial = current_dial

def back_to_dial():
    global current_dial
    global zero_count
    global previous_dial

    if current_dial > 99:
        current_dial -= 100
        if current_dial != 0 and previous_dial != 0:
            zero_count += 1
        back_to_dial()
    elif current_dial < 0:
        current_dial += 100
        if current_dial != 0 and previous_dial != 0:
            zero_count += 1
        back_to_dial()
    else:
        return

def check_rounds(amount: int) -> int:
    global zero_count
    rounds = amount // 100
    zero_count += rounds
    amount -= rounds * 100
    return amount
# Run the code
start()