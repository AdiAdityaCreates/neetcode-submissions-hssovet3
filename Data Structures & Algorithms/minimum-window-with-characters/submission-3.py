from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        need = Counter(t)
        need_count = len(need)

        have = defaultdict(int)
        have_count = 0

        res = float('inf')
        res_l = 0
        res_r = 0

        for r in range(len(s)):
            have[s[r]] += 1

            if have[s[r]] == need[s[r]]:
                have_count += 1

            while have_count == need_count:
                if (r - l + 1) < res:
                    res = (r - l + 1)
                    res_l = l
                    res_r = r

                have[s[l]] -= 1
                if have[s[l]] < need[s[l]]:
                    have_count -= 1
                l += 1

        return "" if res == float('inf') else s[res_l:res_r+1]