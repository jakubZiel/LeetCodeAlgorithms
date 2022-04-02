def integer_break(n : int) -> int:
    cache = {}

    def recurse(n : int) -> int:
        if n in cache:
            return cache[n]

        if n == 1 or n == 0:
            return n
        
        max_product = 0

        for i in range(1, n):        
            left = i
            right = n - i

            left_decision = max(recurse(left), left)
            right_decision = max(recurse(right), right)

            max_product = max(left_decision * right_decision, max_product)
        
        cache[n] = max_product

        return max_product
    return recurse(n)

n = 50

print(integer_break(n))