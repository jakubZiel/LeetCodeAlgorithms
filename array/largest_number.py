from functools import cmp_to_key
from typing import List

def largest_number(numbers : List[int]) -> str:
    numbers = list(map(lambda x : str(x), numbers))

     
    def compare(n1 : str, n2 : str) -> int:
        if n1 + n2 > n2 + n1:
            return 1
        else :
            return -1

    numbers.sort(reverse=True, key=cmp_to_key(compare))

    return "".join(numbers)
numbers = [3, 30, 34, 5, 9]

result = largest_number(numbers)

print(result)