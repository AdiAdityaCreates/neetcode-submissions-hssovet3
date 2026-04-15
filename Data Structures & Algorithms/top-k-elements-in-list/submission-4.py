class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)

        bucket = [[] for  r in range(len(nums)+1)]

        for key, values in freq.items():
            bucket[values].append(key)
        res = []
        for i   in range(len(bucket)-1,-1,-1):
            
            for  j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res
        return res