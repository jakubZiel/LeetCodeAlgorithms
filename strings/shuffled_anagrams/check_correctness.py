from shuffled_anagram import shuffled_anagram, IMPOSSIBLE

def value_counts(word : list) -> dict:
    letter_counts = {}
    for letter in word:
        if letter_counts.__contains__(letter):
            letter_counts[letter] += 1
        else: 
            letter_counts[letter] = 1

    return letter_counts

def check_counts(letters1 : dict, letters2 : dict) -> bool:
    for key in letters1:
        if letters1[key] != letters2[key]:
            return False
    return True

def check_shuffled(word1 : list, word2 : list) -> bool:
    for index, letter in enumerate(word1):
        if word1[index] == word2[index]:
            return False
    return True

if __name__ == "__main__":
    
    #abcdefghijklmnouprstuwxyz
    source = "aaaaaaaaaaaabcdfgheeeeeeeeeeee"
    source = list(source)
    anagram = shuffled_anagram(source)

    print(source)
    print(anagram)

    if (anagram != IMPOSSIBLE):
        print("check counts : " + str(check_counts(value_counts(source), value_counts(anagram))))
        print("check shuffled : " + str(check_shuffled(source, anagram)))