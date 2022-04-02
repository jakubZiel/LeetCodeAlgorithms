from collections import defaultdict

def bulls_and_cows(secret : str, guess : str) -> str:
    bulls = set()
    cows = set()
    wrong_pos = defaultdict(set)
    length = len(secret)

    for i in range(length): 
        if secret[i] == guess[i]:
            bulls.add(i)
        else:
            wrong_pos[secret[i]].add(i)
            

    for i in range(length):
        if not i in bulls:
            if len(wrong_pos[guess[i]]) > 0:
                wrong_pos[guess[i]].pop()
                cows.add(i)

    return f"{len(bulls)}A{len(cows)}B"


secret = "1123123123"
guess = "0111321321"

print(bulls_and_cows(secret, guess))