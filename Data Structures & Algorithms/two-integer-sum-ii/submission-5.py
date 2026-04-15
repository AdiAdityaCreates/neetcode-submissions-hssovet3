class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        res = []
        n = len(numbers)
        l = 0
        r = n-1
        while l < r:
            s = numbers[l] + numbers[r]

            if s == target:
                return [l+1,r+1]
                l += 1
                r -= 1

                while l < r and num[bersl] == numbers[l-1]:
                    l += 1
                while l < r and numbers[r] == numbers[r+1]:
                    r -= 1
            if s > target:
                r -= 1
            else:
                l += 1
        return res