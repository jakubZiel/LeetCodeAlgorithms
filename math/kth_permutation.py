from typing import List

def kth_permutation(n : int, k : int) -> str:
    def permutations(remaining : str) -> List[str]:
   
        if len(remaining) == 1:
            return [remaining]

        result = []
        heads = list(remaining)   

        for head in heads:
            rest = remaining.replace(head, "")

            n_permutations = permutations(rest)

            for index in range(len(n_permutations)):
                n_permutations[index] = head + n_permutations[index]   
            
            result += n_permutations
        return result    
    
    beginning = ""

    for i in range(1, n + 1):
        beginning += str(i)

    return permutations(beginning)


res = kth_permutation(4, 3)
print(len(res))
print(res)