from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    st = []
    never_collisions = []
    for asteroid in asteroids:
        flag = 1
        if len(st) == 0 and asteroid < 0:
            never_collisions.append(asteroid)
            continue
        while st and st[-1] > 0 > asteroid:
            if abs(st[-1]) < abs(asteroid):
                st.pop()
                continue
            elif abs(st[-1]) == abs(asteroid):
                st.pop()
            flag = 0
            break

        if flag:
            st.append(asteroid)

    return never_collisions + st


class Solution:
    pass
