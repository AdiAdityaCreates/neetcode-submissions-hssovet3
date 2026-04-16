class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for A in asteroids:
            alive = True
            
            while stack and stack[-1] > 0 and A < 0:
                if stack[-1] < abs(A):
                    stack.pop()
                elif stack[-1] == abs(A):
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                stack.append(A)
        return stack
