class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        n = len(heights)
        ans = 0
        while l<r:
            w = r-l
            h = min(heights[l],heights[r])
            ans = max(w*h, ans)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return ans