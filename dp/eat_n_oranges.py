def eat_n_oranges(n : int) -> int:

    cache = {}

    def recurse(n : int) -> int:
        if n == 0 or n == 1:
            return n

        if n in cache:
            return cache[n]
        
        mod2 = 1 + n % 2 + recurse((n - n % 2) / 2)
        mod3 = 1 + n % 3 + recurse((n - n % 3) / 3)
        
        cache[n] = min(mod2, mod3)
        
        return cache[n]

    return int(recurse(n))

print(eat_n_oranges(10))