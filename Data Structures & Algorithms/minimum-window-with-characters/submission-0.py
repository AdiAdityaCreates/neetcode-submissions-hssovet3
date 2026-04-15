class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t1 = Counter(t)
        need = defaultdict(int)
        min_len = float('inf')
        res_l, res_r = 0, 0
        l = 0

        for r in range(len(s)):
            if s[r] in t1:
                need[s[r]] += 1

            while need == t1:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res_l, res_r = l, r
                need[s[l]] -= 1
                if need[s[l]] == 0:
                    del need[s[l]]
                l += 1

        return s[res_l:res_r+1] if min_len != float('inf') else ""