from typing import Union

with open("./input.txt", "r") as input_text:
    data = input_text.read().split("\n")

with open("./test_input.txt", "r") as input_text:
    test_data = input_text.read().split("\n")

amount_blue = 14
amount_red = 12
amount_green = 13


def split_line_into_colors(line: str) -> int:
    if len(line) == 0:
        return 0

    relevant_information = line.split(":")
    game_index = relevant_information[0].replace("Game", "").replace(" ", "")
    games = relevant_information[1].split(";")

    for game in games:
        split_game = game.split(",")
        for split in split_game:
            blue_index = split.find("blue")
            red_index = split.find("red")
            green_index = split.find("green")

            if blue_index != -1:
                blue = int(split.replace("blue", "").replace(" ", ""))
                if blue > amount_blue:
                    return 0

            if red_index != -1:
                red = int(split.replace("red", "").replace(" ", ""))
                if red > amount_red:
                    return 0

            if green_index != -1:
                green = int(split.replace("green", "").replace(" ", ""))
                if green > amount_green:
                    return 0

    return int(game_index)


print(sum([split_line_into_colors(line) for line in data]))

