class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        for i in range(n):
            l = i + 1
            r = n - 1
            t = target - numbers[i]

            while l <= r:
                mid = (l + r) // 2

                if numbers[mid] == t:
                    return [i + 1, mid + 1]

                elif numbers[mid] < t:
                    l = mid + 1
                else:
                    r = mid - 1