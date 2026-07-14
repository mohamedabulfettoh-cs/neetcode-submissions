class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        maxi = len(nums) - 1
        while(low <= maxi):
            mid = (low + maxi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                maxi = mid -1
        return -1        
                
                       
        