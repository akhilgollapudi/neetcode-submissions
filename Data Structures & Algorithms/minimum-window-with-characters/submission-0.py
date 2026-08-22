class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left,right = 0,0
        freq_s = {}
        freq_t = {}
        satisfied=0
        min_win_str = ""
        
        for i in range(len(t)):
            freq_t[t[i]] = 1 + freq_t.get(t[i], 0)
        for i in range(len(s)):
            
            freq_s[s[i]] = 1 + freq_s.get(s[i], 0)
            right+=1
            if s[i] in freq_t and freq_s[s[i]] == freq_t[s[i]]:
                satisfied += 1
            while satisfied == len(freq_t):
                if min_win_str == "" or len(s[left:right]) < len(min_win_str):
                    min_win_str = s[left:right]
                if s[left] in freq_t and freq_s[s[left]] == freq_t[s[left]]:
                    satisfied -= 1
                freq_s[s[left]] -= 1
                left +=1
        return min_win_str


