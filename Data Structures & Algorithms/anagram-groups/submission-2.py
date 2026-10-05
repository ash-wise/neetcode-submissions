class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        basket={}

        for x in strs:
            result = sorted(x)
            key = "".join(result)
            if key not in basket:
                basket[key] = []
            basket[key].append(x)
        return list(basket.values())