from typing import List

def paint_house(costs : List[List[int]]) -> int:
    cache = {}
    
    for i in range(0, 3):
        cache[(len(costs) - 1), i] = costs[len(costs) - 1][i]

    def recurse(house : int, color : int):
        if (house, color) in cache:
            return cache[(house, color)]
        
        colors = find_color(color)

        cost0 = recurse(house + 1, colors[0])
        cost1 = recurse(house + 1, colors[1])

        cache[(house, color)] = min(cost0, cost1) + costs[house][color]

        return cache[(house, color)]

    def find_color(color : int) -> int:
        colors = [0, 1, 2]
        return [i for i in colors if i != color]
        

    return min(recurse(0, 0), recurse(0, 1), recurse(0, 2))


costs = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19]
]

print(paint_house(costs))