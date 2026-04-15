class Solution:
    def majorityElement(self, nums: list[int]) -> int:
       
       freq = {}
       for num in nums:

        freq[num] = 1 + freq.get(num,0)

        return max(freq,key = freq.get)