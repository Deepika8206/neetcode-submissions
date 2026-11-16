class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i=0
        while i <n:
            current_index = nums[i] - 1 
            if 1 <= nums[i] <= n and nums[i] != nums[current_index]:
                nums[i],nums[current_index] = nums[current_index] , nums[i]
            else:
                i +=1
        for i in range(n):
            if nums[i] != i+1:
                return i +1 
        return n+1