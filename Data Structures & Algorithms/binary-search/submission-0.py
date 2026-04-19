class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) 
        def binsearch(s, l, r, target):
            m = (l + r) // 2
            if len(s[l:r]) == 1:
                if s[l] == target:
                    return l 
                else:
                    return -1
            else:
                if target > s[m]:
                    return binsearch(s, m+1, r, target)
                else:
                    return binsearch(s, l, m+1, target)
        return binsearch(nums, l, r, target)