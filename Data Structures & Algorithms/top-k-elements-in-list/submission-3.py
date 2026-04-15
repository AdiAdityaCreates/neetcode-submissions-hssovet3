class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        bucket  = [[] for _ in range((n+1))]
        freq =   {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        
        for num ,count  in freq.items():
            bucket[count].append(num)

        res = []
        for i in range(len(bucket)-1,-1,-1):
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res
        return res