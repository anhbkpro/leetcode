from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    st = []
    never_collisions = []
    for asteroid in asteroids:
        if len(st) == 0 and asteroid < 0:  # to handle the case when the first asteroid is negative like [-2, -2, 1, -2]
            never_collisions.append(asteroid)
            continue

        flag = 1
        while st and st[-1] > 0 > asteroid:  # collision happened
            top = st[-1]
            # the left asteroid is destroyed, the right one is still alive, continue collision to the top of the stack
            if abs(top) < abs(asteroid):
                st.pop()
                continue
            elif abs(top) == abs(asteroid):  # both are destroyed
                st.pop()
            flag = 0  # the right asteroid is destroyed, keep the left one
            break

        if flag:
            st.append(asteroid)

    return never_collisions + st


class Solution:
    pass
