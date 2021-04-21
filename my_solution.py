class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def findMax(head: ListNode) -> int:
    if not head:
        return 0
    
    return max(head.value, findMax(head.next))

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))
print(findMax(LL1)) # 5
print(findMax(LL2)) # 7
print(findMax(LL3)) # 0
print(findMax(ListNode(1))) # 1
