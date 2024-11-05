class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ind in asteroids:
            fl = True
            while stack and (ind < 0 and stack[-1] > 0):
                if abs(ind) == abs(stack[-1]):
                    stack.pop()
                    fl = False
                    break
                if abs(ind) > abs(stack[-1]):
                    stack.pop()
                else:
                    fl = False
                    break
            
            if (not stack and fl) or fl:
                stack.append(ind)
            # print(stack)


        return stack