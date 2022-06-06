import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
    list_queue = []
    for list in lists:
        if list is not None:
            list_queue.append((list.val, id(list), list))

    sorted = ListNode("root", None)
    root = sorted


    heapq.heapify(list_queue)

    while (list_queue):
        _, _, min_list = heapq.heappop(list_queue)

        min_list_head : Optional[ListNode] = min_list
        min_list : Optional[ListNode] = min_list.next
        min_list_head.next = None

        sorted.next = min_list_head
        sorted = sorted.next

        if min_list is not None:
            heapq.heappush(list_queue, (min_list.val, id(min_list), min_list))

    return root.next


lists = [[5,7,8],[1,3,4],[2,6]]


lists = [
    ListNode(5, ListNode(7, ListNode(8))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]

sorted = merge_k_lists(lists)
result = []
while sorted is not None:
    result.append(sorted.val)
    sorted = sorted.next

print(result)