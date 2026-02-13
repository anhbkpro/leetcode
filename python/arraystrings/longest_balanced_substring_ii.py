class Solution:
    def longestBalanced(self, s: str) -> int:
        # prefix counts
        a = b = c = 0

        # Maps storing earliest index for each signature:
        # triple: (a-b, a-c)  -> substrings where all three increments are equal
        triple = {(0, 0): -1}

        # pair maps:
        # for a/b pair we require (a-b) equal AND c didn't change => key (a-b, c)
        # similarly for other pairs
        pair_ab = {(0, 0): -1}  # (a-b, c)
        pair_ac = {(0, 0): -1}  # (a-c, b)
        pair_bc = {(0, 0): -1}  # (b-c, a)

        max_len = 0

        # single-character longest run
        prev = None
        run = 0
        max_run = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1

            # keys for the different cases
            key_triple = (a - b, a - c)
            key_ab = (a - b, c)
            key_ac = (a - c, b)
            key_bc = (b - c, a)

            # triple-case: all three increased equally
            if key_triple in triple:
                max_len = max(max_len, i - triple[key_triple])
            else:
                triple[key_triple] = i

            # pair cases (two distinct characters present and the third unchanged)
            if key_ab in pair_ab:
                max_len = max(max_len, i - pair_ab[key_ab])
            else:
                pair_ab[key_ab] = i

            if key_ac in pair_ac:
                max_len = max(max_len, i - pair_ac[key_ac])
            else:
                pair_ac[key_ac] = i

            if key_bc in pair_bc:
                max_len = max(max_len, i - pair_bc[key_bc])
            else:
                pair_bc[key_bc] = i

            # single-character run
            if ch == prev:
                run += 1
            else:
                run = 1
                prev = ch
            if run > max_run:
                max_run = run

        # answer is the best among triple/pair cases and the longest single-char run
        return max(max_len, max_run)
