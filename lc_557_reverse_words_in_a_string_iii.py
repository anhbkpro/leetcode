class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        strs = s.split(' ')
        rv = []
        for item in strs:
            rv.append(item[::-1])

        return ' '.join(rv)

    @staticmethod
    def reverseWords2Pointers(s: str) -> str:
        last_space_index = -1
        n = len(s)
        ch_array = list(s)
        print(ch_array)
        for i in range(n + 1):
            if i == n or s[i] == ' ':
                start_index = last_space_index + 1
                end_index = i - 1
                while start_index < end_index:
                    ch_array[start_index], ch_array[end_index] = ch_array[end_index], ch_array[start_index]
                    start_index += 1
                    end_index -= 1
                last_space_index = i

        return ''.join(ch_array)
