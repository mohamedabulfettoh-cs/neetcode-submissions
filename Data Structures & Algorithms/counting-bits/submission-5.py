class Solution:
    def countBits(self, n: int) -> List[int]:
         nums = [0]*(n+1)
         for i in range (0, n+1):
             nums[i] = nums[i // 2] + (i % 2)
         return nums        