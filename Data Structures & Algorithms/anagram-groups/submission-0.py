class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        check_dict = {}
        
        for idx in range(len(strs)):

            if strs[idx] not in check_dict:

                dummy = []
                dummy.append(strs[idx])
                check_dict[strs[idx]] = 0

                for idx2 in range(idx+1, len(strs)):

                    if strs[idx2] not in check_dict:

                        if sorted(strs[idx]) == sorted(strs[idx2]):

                            dummy.append(strs[idx2])
                            check_dict[strs[idx2]] = 0 

                lst.append(dummy)   

        return lst
