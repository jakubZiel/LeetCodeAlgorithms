def parse(s : str) -> str:
    i = 0
    result = ""

    def parse_number(s : str) -> str:
        number = ""
        i = 0
        while s[i].isdigit():
            number += s[i]
            i += 1
        return number
    
    while i < len(s):
        if s[i].isdigit():
            number = parse_number(s[i:])
            i += len(number) + 1
            k = int(number)
            decoded, parsed = parse(s[i:])
            i += parsed
            result += decoded * k
        elif s[i] == "]":
            return (result, i + 1)
        else :
            result += s[i]
            i += 1        
    return (result, len(result))



encoded = "1[e2[f]]ef"
print(parse(encoded))
