class Solution:
    def maxArea(self, heights: List[int]) -> int:
        watercontained = []
        l = 0
        r = len(heights) -1
        while l < r:
            distancebetween = r-l
            if heights[l] > heights[r]:
                watercontained.append(distancebetween*heights[r])
                r-=1
            elif heights[l] == heights [r]:
                watercontained.append(distancebetween*heights[l])
                r-=1
            elif heights[r] > heights[l]:
                watercontained.append(distancebetween*heights[l])
                l+=1
    
        return max(watercontained)
        
