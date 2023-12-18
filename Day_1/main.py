from functools import reduce

with open("./input.txt", "r") as input_text:
    data = input_text.read().split("\n")


def extract_number(current_line: str) -> int:
    first_digit = None
    second_digit = None

    left = 0
    right = len(current_line) - 1

    while left <= right:
        if current_line[left].isnumeric():
            first_digit = current_line[left]

        if current_line[right].isnumeric():
            second_digit = current_line[right]

        if not first_digit:
            left += 1

        if not second_digit:
            right -= 1

        if first_digit and second_digit:
            break

    if not second_digit and not first_digit:
        return 0

    if not second_digit:
        return int(first_digit)

    if not first_digit:
        return int(second_digit)

    return int(first_digit + second_digit)


print(sum([extract_number(line) for line in data]))

