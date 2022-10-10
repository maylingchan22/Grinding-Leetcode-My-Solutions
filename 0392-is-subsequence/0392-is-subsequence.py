class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_bound, right_bound = len(s), len(t)
        p_left = p_right = 0
        while p_left < left_bound and p_right < right_bound:
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1
        return p_left == left_bound