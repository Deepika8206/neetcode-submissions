class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left<=right:
            mid = (left+right)//2
            currentload = 0
            requireddays = 1
            for i in weights:
                if currentload + i > mid:
                    requireddays +=1
                    currentload = 0
                currentload += i
            if requireddays <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left