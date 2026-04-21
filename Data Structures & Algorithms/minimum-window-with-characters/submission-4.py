class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        thinking of having two pointers
        iterate with the right pointer 
        once the right pointer is on something contained in substring, start checking for
        a valid window
        move the left pointer forward until we have invalid.
        """
        res = False
        subMap = Counter(t)
        curMap = defaultdict(int)
        valid = set()
        window = [-float("inf"), float("inf")]

        l = 0
        for r in range(len(s)):
            if not curMap:
                l = r

            if s[r] in subMap:
                curMap[s[r]] += 1
                if curMap[s[r]] >= subMap[s[r]]:
                    valid.add(s[r])
                while len(valid) >= len(subMap):
                    print(valid)
                    print(l,r)
                    res = True
                    if r - l < window[1] - window[0]:
                        window = [l,r]
                    if s[l] in curMap:
                        curMap[s[l]] -= 1
                        if curMap[s[l]] < subMap[s[l]]:
                            valid.remove(s[l])
                    l += 1

        return s[window[0]:window[1]+1] if res else ""