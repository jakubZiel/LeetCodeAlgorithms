def my_pow(x: float, n: int) -> float:
    cache = {}
    def rec_pow(x : float, n : int) -> float:
        if n in cache:
            return cache[n]
        if n == 0:
            return 1
        if n == 1:
            return x
                    
        if n % 2 == 0:
            result = pow(x, n / 2) * pow(x, n / 2)
        else:
            result = x * pow(x, (n - 1) / 2) * pow(x, (n - 1) / 2)
        
        cache[n] = result
        return result
    return rec_pow(x, n)
    
print(my_pow(-2.0, 2))