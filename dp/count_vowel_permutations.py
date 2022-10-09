def count_vowel_permutation(n: int) -> int:
    cache = {}

    def dp(vowel: str, remaining: int):
        if remaining == 0:
            return 1
        if (vowel,remaining) in cache:
            return cache[(vowel, remaining)]
        
        match vowel:
            case 'a':
                value = dp('e', remaining - 1)
            case 'e':
                value = dp('i', remaining - 1) + dp('a', remaining - 1)
            case 'i':
                value = sum([dp(vowel, remaining - 1) for vowel in list('aeou')])
            case 'o':
                value = dp('i', remaining - 1) + dp('u', remaining - 1)
            case 'u':
                value = dp('a', remaining - 1)

        cache[(vowel, remaining)] = value   
        return value

    return  sum([dp(vowel, n - 1) for vowel in list('aeiou')]) % (1_000_000_000 + 7)

def count_vowel_permutation_dp(n: int) -> int:
    dp = [{key:0 for key in list('aeiou')} for _ in range(0, n)]
    dp[0] = {key:1 for key in list('aeiou')}

    for i in range(1, n):
        for vowel in list('aeiou'):
            match vowel:
                case 'a':
                    value = dp[i - 1]['e']
                case 'e':   
                    value = dp[i - 1]['i'] + dp[i - 1]['a']
                case 'i':
                    value = sum([dp[i - 1][char] for char in list('aeou')])
                case 'o':
                    value = dp[i - 1]['i'] + dp[i - 1]['u']
                case 'u':
                    value = dp[i - 1]['a']
            dp[i][vowel] = value

    return sum([dp[n - 1][vowel] for vowel in list('aeiou')]) % (1_000_000_000 + 7)
n = 5
print(count_vowel_permutation_dp(n))
0