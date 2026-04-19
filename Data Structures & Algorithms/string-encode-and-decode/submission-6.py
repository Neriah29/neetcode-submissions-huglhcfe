class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            if i:
                s += "_" + strs[i]
            else:
                s += strs[i]
            print(s)
        return s

    def decode(self, s: str) -> List[str]:
        return s.split("_")


