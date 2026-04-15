class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        freq = {}
        res = []
        freq =Counter(nums)
        
        for key in freq:
            if freq[key] >=2:
                res.append(key)
        return res