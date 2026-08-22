class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        freq_t = {}

        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1

        freq_s = {}
        satisfied = 0
        required = len(freq_t)

        left = 0
        min_len = float("inf")
        min_start = 0

        for right, c in enumerate(s):

            if c in freq_t:
                freq_s[c] = freq_s.get(c, 0) + 1

                if freq_s[c] == freq_t[c]:
                    satisfied += 1

            while satisfied == required:

                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    min_start = left

                left_char = s[left]

                if left_char in freq_t:
                    if freq_s[left_char] == freq_t[left_char]:
                        satisfied -= 1

                    freq_s[left_char] -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len]