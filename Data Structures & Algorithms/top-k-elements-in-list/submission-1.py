class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = set()
        for n in nums:
            freq[n] += 1
            if freq[n] >= k:
                res.add(n)
        return list(res)
        #for key, val in freq.items():
