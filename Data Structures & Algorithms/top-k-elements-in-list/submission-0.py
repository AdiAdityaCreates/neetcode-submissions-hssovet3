from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = Counter(nums)

        for _ in range(k):
            max_key = max(freq, key=freq.get)  
            ans.append(max_key)
            del freq[max_key]  

        return ans