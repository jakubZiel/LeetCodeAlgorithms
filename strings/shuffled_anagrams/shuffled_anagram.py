from itertools import count
from sortedcontainers.sortedlist import SortedList
from LetterGroup import LetterGroup

IMPOSSIBLE = "IMPOSSIBLE"

def find_max(letters : SortedList) -> LetterGroup: 
    return letters[len(letters) - 1]

def second_max(letters : SortedList) -> LetterGroup:
    return letters[len(letters) - 2] if len(letters) > 1 else None
                
def remove(group_index : int, letters : SortedList):
    group : LetterGroup = letters[group_index]

    if group.count == 1:
        letters.pop(group_index)
    else:
        group.count -= 1
        group.letters.pop(0)

def count_letters(source : list) -> dict:
    letters = {}

    for index, letter in enumerate(source):
        if letters.__contains__(letter):
            letters[letter] += [index]
        else:
            letters[letter] = [index]
    return letters

def shuffled_anagram(source : str) -> str: 
    
    letters = count_letters(source)
    
    letter_groups = SortedList()

    for key, value in letters.items():
        letter_groups.add(LetterGroup(len(value), key, value))
    
    anagram = list(source)
    source = list(source)
    
    while len(letter_groups) > 0:
        first = find_max(letter_groups)
        second = second_max(letter_groups)
        
        if second == None:
            return IMPOSSIBLE

        index1 = first.letters[0]
        index2 = second.letters[0]
        
        anagram[index2] = anagram[index1]
        anagram[index1] = second.letter

        length = len(letter_groups)

        remove(len(letter_groups) - 1, letter_groups)
        group_index = len(letter_groups) - 1 if length > len(letter_groups) else len(letter_groups) - 2
        remove(group_index, letter_groups)

    return anagram