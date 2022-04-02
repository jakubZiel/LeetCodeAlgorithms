from typing import List

def is_robot_bounded(instructions : str) -> bool:
    start_pos = [0, 0]
    pos = [0, 0]
    start_dir = dir = 0

    directions = {0 : [0, 1], 1 : [1, 0], 2 : [0, -1], 3 : [-1, 0]}

    for instruction in  instructions:
        if instruction == "G":
            pos[0] += directions[dir][0]
            pos[1] += directions[dir][1]
        elif instruction ==  "L":
            dir = (dir - 1) % 4
        else :
            dir = (dir + 1) % 4

    if start_pos == pos:
        return True

    if start_dir != dir:
        return True
    return False

instructions = "GGGGLL"

print(is_robot_bounded(instructions))