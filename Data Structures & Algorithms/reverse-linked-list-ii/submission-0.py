class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head   # 🔥 missing in your code

        prev = dummy

        # 1. move prev to (left-1) position
        for _ in range(left - 1):
            prev = prev.next

        # 2. reverse from left to right
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next