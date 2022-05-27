def remove_k_adjacent(string : str, k : int) -> str:

    stack = []

    for i in range(0, len(string)):

        if not stack:
            stack.append((string[i], 1))

        elif stack[len(stack) - 1][0] == string[i]:
            if stack[len(stack) - 1][1] == k - 1:
                stack.pop()
            else:
                stack[len(stack) - 1] = (string[i], stack[len(stack) - 1][1] + 1)
        else:    
            stack.append((string[i], 1))

    result = ""

    for element in stack:
        char, count = element

        result += char * count

    return result


string = "deeedbbcccbdaa"
k = 3

print(remove_k_adjacent(string, k))