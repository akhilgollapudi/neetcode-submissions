class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_window_len = 0
        max_freq = 0
        start = 0
        freq = {}

        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            max_freq = max(max_freq, freq[s[i]])

            while (i - start + 1) - max_freq > k:
                freq[s[start]] -= 1
                start += 1

            max_window_len = max(max_window_len, i - start + 1)

        return max_window_len