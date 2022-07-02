from typing import List


def search_suggestion(products: List[str], search_word: str) -> List[List[str]]:
    products.sort()
    results = []

    left = 0
    right = len(products)

    prefix: str = ""

    for char in search_word:
        prefix += char

        while left < len(products) and not products[left].startswith(prefix):
            left += 1
        while right > 0 and not products[right - 1].startswith(prefix):
            right -= 1

        result = []
        i = left
        while i < right and i < left + 3:
            result.append(products[i])
            i += 1

        results.append(result)
    
    return results


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mousep"


res = search_suggestion(products, search_word=searchWord)

for r in res:
    print(r)