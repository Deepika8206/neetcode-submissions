class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area =0
        for i in range(len(heights)+1):
            if i == len(heights):
                currentheight = 0
            else:
                currentheight = heights[i]
            while stack and heights[stack[-1]] > currentheight:
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                area = height * width
                max_area = max(area,max_area)
            if i < len(heights):
                stack.append(i)
        return max_area