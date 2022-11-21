from typing import List, Tuple


def valid_parenthesis(string: str) -> bool:

    stack: List[Tuple[int, int]] = []
    wildcard_stack: List[int] = []

    chars = list(string)
    n = len(string)
    
    i = 0

    while i < n:
        curr = chars[i]

        match curr:
            case '*':
                wildcard_stack.append(i)
            case '(':
                stack.append(i)
            case ')':
                if stack:
                    stack.pop()
                else:
                    if wildcard_stack:
                        wildcard_stack.pop()
                    else:
                        return False
        i += 1

    if not stack:
        return True

    wildcard_index = 0
    par_index = 0

    while par_index < len(stack) and wildcard_index < len(wildcard_stack):
        left_par = stack[par_index]
        curr_wildcard = wildcard_stack[wildcard_index]

        if left_par < curr_wildcard:
            par_index += 1
            wildcard_index += 1
        else:
            wildcard_index += 1

    return par_index == len(stack)
        

string = "*()()(()()"

print(valid_parenthesis(string))