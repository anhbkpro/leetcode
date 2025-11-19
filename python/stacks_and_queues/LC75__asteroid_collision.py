from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            right_hand_asteroid_win = True
            while stk and stk[-1] > 0 and asteroid < 0:
                top = stk[-1]
                if abs(top) < abs(asteroid):
                    stk.pop()
                    continue  # continue with the next asteroid in the stack.
                elif abs(top) == abs(asteroid):
                    stk.pop()

                right_hand_asteroid_win = False
                break

            if right_hand_asteroid_win:
                stk.append(asteroid)

        return stk
