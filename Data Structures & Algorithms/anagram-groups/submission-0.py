class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        baskets = {}

        for x in strs:
            result = sorted(x)
            key = "".join(result)
            if key not in baskets:
                baskets[key] = []
            baskets[key].append(x)
        return (list(baskets.values()))