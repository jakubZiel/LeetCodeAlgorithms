from dataclasses import dataclass, field

from sortedcontainers.sortedlist import SortedList

@dataclass(order=True)
class LetterGroup:
    count : int
    letter : str = field(compare=False)
    letters : list = field(compare=False)