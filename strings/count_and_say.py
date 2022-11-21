from typing import List, Tuple

def count_and_say(n: int) -> str:

    if n == 0:
        return None

    num = "1"

    for _ in range(0, n - 1):
        counter: List[Tuple[str, int]] = [(num[0], 1)]
        counter_index = 0

        for i in range(1, len(num)):
            
            if num[i] == num[i - 1]:
                counter[counter_index] = (num[i], counter[counter_index][1] + 1)
            else:
                counter.append((num[i], 1))
                counter_index += 1
        
        chunks: List[str] = []

        for ele in counter:
            chunks.append(str(ele[1]) + ele[0])            
        
        num = "".join(chunks)
    return num

if count_and_say(10) == "13211311123113112211":
    print("OK")
else:
    print("FAIL")