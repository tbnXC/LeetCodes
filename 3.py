class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2: return len(s)
        maxSubstrLen = 0
        strPointer = 0
        while (strPointer<len(s)-maxSubstrLen): ##-max optimization
            for i in range (strPointer, len(s)):
                print (s[strPointer:i], s[i])
                if s[i] in s[strPointer:i]:
                    if (maxSubstrLen < i-strPointer): maxSubstrLen = i-strPointer
                    break
            print("ENDCHECK", s[strPointer:-1], s[i])
            if s[i] not in s[strPointer:-1]:
                if (maxSubstrLen < i-strPointer+1): maxSubstrLen = i-strPointer+1
            strPointer+=1
        return maxSubstrLen

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s)<2: return len(s)
        l = 0
        r = 0
        maxSubStrLen = 0
        while l<len(s)-maxSubStrLen and r<len(s):
            print(s, l, r)
            if s[r] in s[l:r]: 
                if r-l>maxSubStrLen: maxSubStrLen = r-l
                l = s.index(s[r], l) + 1
            r+=1
        return max(r-l, maxSubStrLen)

s = Solution1()
string = " "
print(s.lengthOfLongestSubstring(string))

