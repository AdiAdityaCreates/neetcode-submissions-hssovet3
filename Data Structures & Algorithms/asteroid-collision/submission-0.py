class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and a < 0:
                if stack[-1] < abs(a):
                    stack.pop()   # top destroyed
                elif stack[-1] == abs(a):
                    stack.pop()   # both destroyed
                    alive = False
                else:
                    alive = False  # current destroyed

            if alive:
                stack.append(a)

        return stack