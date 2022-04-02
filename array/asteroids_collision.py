from typing  import List

def asteroids_collision(asteroids : List[int]) -> List[int]:
    left = []
    right = []
    
    def asteroid(dir : str) -> int:
        if dir == "L":
            return abs(asteroids[left[len(left) - 1]])
        else:
            return abs(asteroids[right[len(right) - 1]])

    i = 0

    while i < len(asteroids):

        if asteroids[i] < 0:
            right.append(i)
        else:
            left.append(i)
            
        while left and right:
            left_first = asteroid("L")
            right_first = asteroid("R")

            if left[len(left) - 1] > right[len(right) - 1]:
                break

            if left_first == right_first:
                left.pop()
                right.pop()
            elif left_first > right_first:
                right.pop()
            else:
                left.pop()
        i += 1

    return list(map(lambda i : asteroids[i], right)) + list(map(lambda i : asteroids[i], left))


asteroids = [-1, 5, 10, 12, -5, -50, 20, 4, 43]

print(asteroids_collision(asteroids))