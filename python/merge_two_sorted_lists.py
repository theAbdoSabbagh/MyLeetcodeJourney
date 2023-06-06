from typing import Optional
from rich import print

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"<ListNode val={self.val} next={self.next}>"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first_dump = list1
        first_list = []
        while first_dump is not None:
            if first_dump.val is None:
                break
            first_list.append(first_dump.val)
            first_dump = first_dump.next

        second_dump = list2
        second_list = []
        while second_dump is not None:
            if second_dump.val is None:
                break
            second_list.append(second_dump.val)
            second_dump = second_dump.next

        merged_list = first_list + second_list
        if len(merged_list) == 0:
            return
        merged_list.sort()
        
        first_node = ListNode(val=merged_list[0])

        # Nest ListNode objects inside each other
        current_node = first_node
        for i in range(len(merged_list)):
            if i == 0:
                continue
            new_node =  ListNode(val = merged_list[i])
            current_node.next = new_node
            current_node = new_node

        return first_node

# Variation 1
print(Solution().mergeTwoLists(
    ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None))),
    ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))
))  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

# Variation 2
print(Solution().mergeTwoLists(
    ListNode(val=5, next=ListNode(val=6, next=ListNode(val=7, next=None))),
    ListNode(val=8, next=ListNode(val=9, next=ListNode(val=10, next=None)))
))  # Output: 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None

# Variation 3
print(Solution().mergeTwoLists(
    ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=None))),
    ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))
))  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

# Variation 4
print(Solution().mergeTwoLists(
    ListNode(val=9, next=ListNode(val=8, next=ListNode(val=7, next=None))),
    ListNode(val=6, next=ListNode(val=5, next=ListNode(val=4, next=None)))
))  # Output: 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> None

# Variation 5
print(Solution().mergeTwoLists(
    ListNode(val=1, next=ListNode(val=3, next=ListNode(val=5, next=None))),
    ListNode(val=2, next=ListNode(val=4, next=ListNode(val=6, next=None)))
))  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# Variation 6
print(Solution().mergeTwoLists(
    ListNode(val=5, next=ListNode(val=10, next=ListNode(val=15, next=None))),
    ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=None)))
))  # Output: 1 -> 2 -> 3 -> 5 -> 10 -> 15 -> None

# Variation 7
print(Solution().mergeTwoLists(
    ListNode(val=7, next=ListNode(val=14, next=ListNode(val=21, next=None))),
    ListNode(val=3, next=ListNode(val=6, next=ListNode(val=9, next=None)))
))  # Output: 3 -> 6 -> 7 -> 9 -> 14 -> 21 -> None

# Variation 8
print(Solution().mergeTwoLists(
    ListNode(val=10, next=ListNode(val=20, next=ListNode(val=30, next=None))),
    ListNode(val=15, next=ListNode(val=25, next=ListNode(val=35, next=None)))
))  # Output: 10 -> 15 -> 20 -> 25 -> 30 -> 35 -> None

# Variation 9
print(Solution().mergeTwoLists(
    ListNode(val=2, next=ListNode(val=4, next=ListNode(val=6, next=None))),
    ListNode(val=1, next=ListNode(val=3, next=ListNode(val=5, next=None)))
))  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# Variation 10
print(Solution().mergeTwoLists(
    ListNode(val=5, next=ListNode(val=15, next=ListNode(val=25, next=None))),
    ListNode(val=10, next=ListNode(val=20, next=ListNode(val=30, next=None)))
))  # Output: 5 -> 10 -> 15 -> 20 -> 25 -> 30 -> None

# Variation 10
print(Solution().mergeTwoLists(
    ListNode(val=None, next=None),
    ListNode(val=None, next=None),
))  # []