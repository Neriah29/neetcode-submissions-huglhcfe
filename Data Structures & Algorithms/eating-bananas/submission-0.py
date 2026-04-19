import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = math.ceil(sum(piles)/h)
        max_rate = max(piles)

        def pile(min_rate, max_rate):
            rate = (min_rate + max_rate) // 2
            if min_rate > max_rate:
                return rate + 1
            h_check = 0
            for i in piles:
                h_check += math.ceil(i/rate)
            if h_check == h:
                return rate
            elif h_check > h:
                return pile(rate + 1, max_rate)
            else:
                return pile(min_rate, rate - 1)
        return pile(min_rate, max_rate)

