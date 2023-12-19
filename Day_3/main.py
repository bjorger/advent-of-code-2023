with open("./input.txt", "r") as input_text:
    data = input_text.read().split("\n")

with open("./test_input.txt", "r") as input_text:
    test_data = input_text.read().split("\n")


def calculate_part_numbers(data: list[str]) -> list[int]:
    valid_numbers = []

    for i in range(len(data)):
        j = 0
        while j < len(data[i]):
            # if data is numeric, we need to check if anything is adjacent to it
            print(f"j before if: {j}")
            if data[i][j].isnumeric():
                # first check what the number is, and how long it is
                temp = j
                number = data[i][j]
                print(f"j before compiling number: {j}")
                while temp < len(data[i]) - 1 and data[i][temp + 1].isnumeric():
                    number += data[i][temp + 1]
                    temp += 1

                j += temp
                print(f"j after compiling number: {j}")

                valid_numbers.append(int(number))
            j += 1
    return valid_numbers


print(calculate_part_numbers(test_data))
