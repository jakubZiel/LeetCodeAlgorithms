def edit_distance(word1 : str, word2 : str) -> int:
    
    cache = {}

    def recurse(ptr1 : int, ptr2 : int) -> int:
        
        if ptr1 == len(word1) - 1 and ptr2 == len(word2) - 1:
            return 0
        
        if ptr1 == len(word1) - 1:
            return len(word2) - ptr2

        if ptr2 == len(word2) - 1:
            return len(word1) - ptr1

        if (word1[ptr1] == word2[ptr2]):
            cache[(ptr1, ptr2)] = recurse(ptr1 + 1, ptr2 + 1)
        else:
            insert = recurse(ptr1 + 1, ptr2) + 1
            delete = recurse(ptr1, ptr2 + 1) + 1
            replace = recurse(ptr1 + 1, ptr2 + 1) + 1

            cache[((ptr1, ptr2))] = min(insert, replace, delete)

        return cache[(ptr1, ptr2)]    

    return recurse(0, 0)


print(edit_distance("ab", "acdddd"))

