class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            result += 1
        return left << result