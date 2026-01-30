class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        vol = 0

        while l < r:
            minVal = min(heights[l], heights[r])
            currVol = minVal * (r-l)
            if currVol > vol:
                vol = currVol
            
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return vol