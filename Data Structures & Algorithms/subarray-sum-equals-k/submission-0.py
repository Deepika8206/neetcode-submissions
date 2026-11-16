class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix =0
        result = 0
        count = {0:1}
        for num in nums:
            prefix += num
            if prefix - k in count:
                result += count[prefix -k]
            count[prefix] = count.get(prefix , 0) +1
        return result