class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_window_len = 0
        start = 0
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            max_freq = max(freq.values())
            cur_window_len = i - start + 1
            replacement_needed = cur_window_len - max_freq
            while replacement_needed > k:
                freq[s[start]] -= 1
                start += 1
                cur_window_len = i - start + 1
                max_freq = max(freq.values())
                replacement_needed = cur_window_len - max_freq
            max_window_len = max(cur_window_len,max_window_len)
        return max_window_len
                