from audioop import mul
from typing import Dict, Tuple

def number_of_atoms(chain : str) -> str:

    counts = {}

    def update_dict(update : Dict[str, int]) -> None:
        for key in update.keys:
            counts[key] = 1 if not key in counts else counts[key] + update[key]

    def multiply_dict(count : Dict[str, int], multiply : int):
        for key in count.keys:
            count[key] *= multiply

    def parse_number(s : str) -> str:
        number = ""
        i = 0
        while s[i].isdigit():
            number += s[i]
            i += 1
        return number

    def parse(chain : str) -> Tuple(str, Dict[str, int]):
        i = 0
        counts = {}

        while i < len(str) :
                        
            if chain[i] == "(":
                parsed, parsed_dict = parse(chain[i:])
                i += len(parsed)
                update_dict(parsed_dict)

            elif chain[i].isdigit():
                number = parse_number()
                i += len(number)
                number = int(number)

            elif chain[i] == ")":
                i += 1
                number = parse_number([chain[i:]])
                i+= len(number)
                multiply_dict(counts, int(number))
                break

        return (chain[0:i], counts)

    i = 0
    #TODO 
    while i < len(chain):

        if chain[i].isalpha() and i < len(chain) - 1 and chain[i + 1].isnumeric():
            count = parse_number()
            i += len(count)
            count = int(count)
            counts[chain[i]] = 1 if counts[chain[i]] == None else counts[chain[i]] + count
        elif chain[i].isalpha():
            counts[chain[i]] = 1 if counts[chain[i]] == None else counts[chain[i]] + 1
            
    return parse(chain)