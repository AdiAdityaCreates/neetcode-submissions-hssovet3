from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # (index, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index   # extend left boundary

            stack.append((start, h))

        n = len(heights)

        for i, h in stack:
            maxArea = max(maxArea, h * (n - i))

        return maxArea