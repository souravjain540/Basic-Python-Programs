class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next

# Example Usage:
# l1 = ListNode(1, ListNode(2, ListNode(4)))
# l2 = ListNode(1, ListNode(3, ListNode(4)))
# result = merge_two_lists(l1, l2)
