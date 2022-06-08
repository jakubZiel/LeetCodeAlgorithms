from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_node_groups(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    length = 0
    tmp = head

    while tmp:
        length += 1
        tmp = tmp.next

    groups = length // k
    reversed_groups = 0
    root = ListNode("root", head) 

    beg_slot = root
    curr = head

    while reversed_groups < groups:
        head_rev = None

        for i in range(0, k):
            if i == 0:
                first_reversed = curr
            if i == k - 1:
                end_slot = curr.next

            curr_next = curr.next
            curr.next = head_rev
            head_rev = curr
            curr = curr_next
        
        beg_slot.next = head_rev
        first_reversed.next = end_slot

        beg_slot = first_reversed
        reversed_groups += 1
    return root.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)


print(reverse_k_node_groups(head, 2))