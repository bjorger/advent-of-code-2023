import re

with open("./input.txt", "r") as input_text:
    data = input_text.read().split("\n")

written_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def find_all_indexes(current_line: str, number: str) -> [int]:
    return [m.start() for m in re.finditer(number, current_line)]


def replace_written_number_with_digit(current_line: str) -> str:
    occurring_numbers = {}

    for number in written_numbers:
        number_index = find_all_indexes(current_line, number)
        for idx in number_index:
            occurring_numbers[idx] = str(written_numbers.index(number) + 1)

    sorted_indexes = sorted(occurring_numbers.keys())
    new_numbers = ""

    for index in range(len(current_line)):
        if index in sorted_indexes:
            new_numbers += occurring_numbers[index]
        elif current_line[index].isnumeric():
            new_numbers += current_line[index]

    return new_numbers


def answer(first_digit: str, second_digit: str) -> int:
    if not second_digit and not first_digit:
        return 0

    if not second_digit:
        return int(first_digit)

    if not first_digit:
        return int(second_digit)

    return int(first_digit + second_digit)


def extract_number(current_line: str) -> int:
    first_digit = None
    second_digit = None
    current_line = replace_written_number_with_digit(current_line)
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

    value = answer(first_digit, second_digit)
    return value


test_data = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

# print(extract_number("nlnineeightmndkqz8nineonenrqm"))

# print(sum([extract_number(line) for line in test_data]))

print(sum([extract_number(line) for line in data]))
