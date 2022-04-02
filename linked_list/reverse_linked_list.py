
from email import header


class Node:
    def __init__(self, val : int):
        self.val = val
        self.next = None


def reverse_linked_list(head : Node):
    curr = head
    head_rev = None

    while curr != None :
        curr_next = curr.next
        curr.next = head_rev
        head_rev = curr
        curr = curr_next

    return head_rev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

reverse_linked_list(head)


