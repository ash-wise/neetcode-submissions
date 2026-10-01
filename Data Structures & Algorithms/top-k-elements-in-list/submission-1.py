class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        basket = {}

        for x in nums:
            if x not in basket:
                basket[x] = 1
            else:
                basket[x] += 1
        sort = sorted(basket, key=basket.get)
        reno = sort[-k:]

        return reno