class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            while stack and (temperatures[i] > temperatures[stack[-1]]):
                days = i-stack[-1]
                output[stack[-1]] = days
                stack.pop()
            stack.append(i)
        return output