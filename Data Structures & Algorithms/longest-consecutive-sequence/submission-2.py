class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(set(nums))
        max_count = 0
        counter = 1
        flag = False
        for idx in range(len(sort)-1):
            if sort[idx +1] == sort[idx] + 1:
                flag = True
            else:
                flag = False
            if flag:
                counter += 1
            else:
                counter = 0
            if counter > max_count:
                max_count = counter
            if max_count == 0:
                max_count = 1
        return max_count
            

            
        