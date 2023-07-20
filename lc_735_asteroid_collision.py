from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    st = []
    never_collisions = []
    for asteroid in asteroids:
        if len(st) == 0 and asteroid < 0:  # to handle the case when the first asteroid is negative like [-2, -2, 1, -2]
            # so never_collisions will be [-2, -2] (asteroids that will never collide with each other on the right side)
            never_collisions.append(asteroid)
            continue

        flag = 1
        while st and st[-1] > 0 > asteroid:  # collision happened
            top = st[-1]
            # If the `asteroid` is bigger than the asteroid on the top, then this asteroid on the top will explode,
            # and we will pop it from the stack.
            if abs(top) < abs(asteroid):
                st.pop()
                continue
            # If the `asteroid` has the same size as the asteroid on the top, then both will explode. Hence, we will
            # pop it from the stack; also, we will mark `flag` as `false` because this `asteroid` will also explode,
            # and hence we won't save it into the stack.
            elif abs(top) == abs(asteroid):  # both are destroyed
                st.pop()
            # If the `asteroid` is smaller than the asteroid on the top, then the asteroid on the top will not
            # explode, so we will not pop it. But the `asteroid` will explode, and thus we will mark `flag` as `false`.
            flag = 0  # the right asteroid is destroyed, and we will not save it into the stack
            break

        if flag:
            st.append(asteroid)

    return never_collisions + st


class Solution:
    pass
