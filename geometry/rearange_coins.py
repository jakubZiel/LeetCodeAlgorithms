from math import sqrt

def rearange_coins(coins : int) ->  int:

    a = 0.5
    b = 0.5
    c = -coins

    top = -b + sqrt(b * b - 4 * a * c)
    bottom = 2 * a
    stairs = top / bottom
    
    return int(stairs)


print(rearange_coins(8))