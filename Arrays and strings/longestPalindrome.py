class Solution:
    def longestPalindrome(self, s: str) -> str:

        indices = [0, 0]
        maxCount = 0
        longest = ''
        
        for i in range(len(s)):
            for j in range(len(s)-1, i-1, -1):
                if(s[i] == s[j]):
                    tmp = s[i:j+1] 
                    if(len(tmp) > maxCount and tmp == tmp[::-1]):
                        maxCount = len(tmp)
                        longest = tmp
        return longest

#########

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) < 1):
            return(s)
        
        start = 0
        end = 0
        maxCount = 0
        
        def expandFromMiddle(string, left, right):

            while(left >= 0 and right < len(string) and string[left] == string[right]):
                left -= 1
                right += 1
            return(right - left - 1)


        for i in range(len(s)):
            expansion1 = expandFromMiddle(s, i, i)
            expansion2 = expandFromMiddle(s, i, i+1) 
            maxLen = max(expansion1, expansion2)

            if(maxLen > end - start):
                start = i - ((maxLen - 1) // 2)
                end = i + (maxLen // 2)


        return(s[start:end+1])