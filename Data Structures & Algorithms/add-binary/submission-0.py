class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        
        # Pointers for both strings starting at the last character
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            # Add digit from string 'a' if pointer is within bounds
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            # Add digit from string 'b' if pointer is within bounds
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # The digit we append is total modulo 2 (either '0' or '1')
            res.append(str(total % 2))
            
            # Calculate the new carry
            carry = total // 2
            
        # Reverse the result list and join it into a string
        return "".join(reversed(res))