class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sum = 0
        for i in range(len(haystack)):
            if haystack[i] in needle:
                return i
        return -1
            
                
                
                
c  = Solution()
print(c.strStr("hello", "r1"))     