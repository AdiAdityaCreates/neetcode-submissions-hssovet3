class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        alive = True

        for A in asteroids:
            alive = True
            if  A < 0:
                while stack and stack[-1] > 0:
                    if abs(stack[-1]) == abs(A):
                        stack.pop()
                        alive = False
                        break
                    elif abs(stack[-1]) < abs(A):
                        stack.pop()
                    else:
                        alive = False
                        break
            if alive:
                stack.append((A))
        return stack