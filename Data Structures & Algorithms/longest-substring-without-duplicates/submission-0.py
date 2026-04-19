class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0 
        u = []
        for i in s:
            u.append(i)
            if len(u) > len(set(u)):
                u.clear()
                u.append(i)
            length = max(len(u), length)
        return length



