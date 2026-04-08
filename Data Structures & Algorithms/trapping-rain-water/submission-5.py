class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        max_left, max_right = [height[0]], [height[-1]]
        length = len(height)
        if length < 3:
            return 0
        l, r = 0, length
        for i in range(2,length - 1):
            #print(i)
            max_left.append(max(height[i-1], max_left[i-2]))
            max_right.append(max(height[length - i], max_right[i-2]))
        max_right.reverse()
        print(max_left)
        print(max_right)
        for i in range(len(max_left)):
            wall = min(max_left[i], max_right[i])
            if wall > height[i + 1]:
                volume += wall - height[i + 1]
            print(i, volume)
        return volume
