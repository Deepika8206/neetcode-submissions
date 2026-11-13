class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] +=1 
            else:
                count[nums[i]] = 1
        sorted_count = sorted(count,key = count.get , reverse = True)
        return sorted_count[:k]

            