class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for element in strs:
            s += element + " "
        return s

    def decode(self, s: str) -> List[str]:
        return s.split()
