class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()  # stores indices, largest value at front
        res = []
        l = 0

        for r in range(len(nums)):
            # remove smaller elements from back
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            # remove left element if out of window
            if dq[0] < l:
                dq.popleft()

            if r - l + 1 == k:
                res.append(nums[dq[0]])  # front is always the max
                l += 1

        return res