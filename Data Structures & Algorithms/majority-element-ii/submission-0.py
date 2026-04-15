class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq = {}
        res = []
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        
        for key in freq:
            if freq[key] >=3:
                res.append(key)
        return res