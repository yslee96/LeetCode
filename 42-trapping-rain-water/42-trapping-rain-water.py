class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        
        for i in range(len(height)):
            print("i:",i)
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                print(top)
                if not len(stack):
                    break
                
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
                print("volume:", volume)
            stack.append(i)
        return volume