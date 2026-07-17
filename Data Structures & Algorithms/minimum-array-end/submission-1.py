class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1  
        result = x
        i = j = 0
        while (n >> j) != 0:
            
            if not (result >> i) & 1:
                if (n >> j) & 1:
                    result |= (1 << i)
                j += 1
            i += 1
        return result