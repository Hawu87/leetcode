class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # if len(s) == 1:
        #     return 1
        myset = set()
        maxval = 0
        l = r = 0
        while r < len(s):
            if s[r] not in myset:
                myset.add(s[r])
                r += 1
            else:
                while s[r] in myset:
                    myset.remove(s[l])
                    l += 1
            maxval = max(maxval, r - l)
        
        return maxval