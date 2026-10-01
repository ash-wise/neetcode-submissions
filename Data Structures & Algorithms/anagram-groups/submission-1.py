class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        basket = {}

        for x in strs:
            sort = sorted(x)
            key = "".join(sort)
            if key not in basket:
                basket[key] = []
            basket[key].append(x)
        return (list(basket.values()))