from typing import List

def destroy_asteroids(asteroids : List[int], mass : int) -> bool:
    asteroids.sort()

    for asteroid in asteroids:
        if asteroid <= mass:
            mass += asteroid
        else:
            return False
    return True


mass = 10
asteroids = [11, 5, 12, 123, 34]

print(destroy_asteroids(asteroids, mass))