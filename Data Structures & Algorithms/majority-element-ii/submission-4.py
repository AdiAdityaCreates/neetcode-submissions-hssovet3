class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        freq = {}
        res = []
        freq =Counter(nums)
        
        for key in freq:
            if n == 1:
                res.append(key)
                return res
            else:
                if freq[key] >=2:
                    res.append(key)
        return res