class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        basket = {}

        for x in strs:
            sort = sorted(x)
            new = "".join(sort)

            if new not in basket:
                basket[new] = []
            basket[new].append(x)
        return (list(basket.values()))