class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict ={"}" : "{", "]" : "[", ")" : "("}
        # exception i guess
        if s[0] in valid_dict:
            return False
        left = []

        for bracket in s:
            if bracket in valid_dict:
                if left.pop() != valid_dict[bracket]:
                    return False 
            else:
                left.append(bracket)
        
        return True