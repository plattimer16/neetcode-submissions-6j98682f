class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        res = 0
        if length < 3:
            return 0
        l, r = 0, length - 1
        maxLeft, maxRight = height[l], height[r]
        while l < r:
            if maxLeft > maxRight:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
            else:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
        return res