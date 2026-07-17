class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1  # we need to distribute the bits of (n-1) into the zero-bit slots of x
        result = x
        i = j = 0
        while (n >> j) != 0:
            # find next zero-bit position in result
            if not (result >> i) & 1:
                if (n >> j) & 1:
                    result |= (1 << i)
                j += 1
            i += 1
        return result