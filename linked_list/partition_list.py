from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: Optional[ListNode], x: int):
    greater_than: ListNode = ListNode(None)
    less_than: ListNode = ListNode(None)
    
    greater_than_head = greater_than
    less_than_head = less_than

    while head is not None: 
        next = head.next
        head.next = None

        if head.val < x:
            less_than.next = head
            less_than = head
        else:
            greater_than.next = head
            greater_than = head
        head = next
    
    less_than.next = greater_than_head.next

    return less_than_head.next



head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2, None))))))
head = partition(head, 3)

result = []
while head is not None:
    result.append(head.val)
    head = head.next

print(result)


