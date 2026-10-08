class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = s.lower()

        basket = ""

        for x in new:
            if x.isalnum():
                basket += x

        left, right = 0, len(basket) - 1

        while left <= right:
            if basket[left] == basket[right]:
                left += 1
                right -= 1
            else:
                return False
        return True