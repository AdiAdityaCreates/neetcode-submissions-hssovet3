class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t1 = Counter(t)
        need = defaultdict(int)
        have, need_count = 0, len(t1)  # need_count = unique chars in t
        min_len = float('inf')
        res_l, res_r = 0, 0
        l = 0

        for r in range(len(s)):
            if s[r] in t1:
                need[s[r]] += 1
                if need[s[r]] == t1[s[r]]:  # this char is now satisfied
                    have += 1

            while have == need_count:        # all chars satisfied
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res_l, res_r = l, r
                need[s[l]] -= 1
                if s[l] in t1 and need[s[l]] < t1[s[l]]:
                    have -= 1               # this char no longer satisfied
                l += 1

        return s[res_l:res_r+1] if min_len != float('inf') else ""